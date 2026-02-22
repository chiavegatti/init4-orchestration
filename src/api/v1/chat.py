import httpx
from fastapi import APIRouter, Request, Depends, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime
import json

from src.core.config import settings
from src.db.session import get_db
from src.models.request import RequestLog
from src.policy.engine import PolicyEngine
from src.policy.cost import CostEngine

router = APIRouter()


def log_transaction_to_db(
    db: Session,
    request_data: dict,
    response_data: dict,
    status: str,
    latency_ms: int,
    error_msg: str = None,
):
    # Try to extract the requested model from the proxy response or payload
    routed_model = response_data.get("model", "unknown") if response_data else "unknown"
    requested_model = request_data.get("model", "unknown")

    # Metadata extracted from the client's payload (task_type etc)
    metadata = request_data.get("metadata", {})
    task_type = metadata.get("task_type", "unassigned")
    tenant_id = metadata.get("tenant_id", None)

    # Token extraction from standard OpenAI response
    usage = response_data.get("usage", {}) if response_data else {}
    input_tokens = usage.get("prompt_tokens", 0)
    output_tokens = usage.get("completion_tokens", 0)

    # Calculate estimated cost using CostEngine
    estimated_cost = float(
        CostEngine.calculate_cost(routed_model, input_tokens, output_tokens)
    )

    new_log = RequestLog(
        timestamp=datetime.utcnow(),
        tenant_id=tenant_id,
        task_type=task_type,
        requested_model=request_data.get(
            "_original_requested_model", requested_model
        ),  # Grab real requested model if we mutated it
        routed_model=routed_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        estimated_cost=estimated_cost,
        latency_ms=latency_ms,
        status=status,
        error_message=error_msg,
    )

    db.add(new_log)
    db.commit()


@router.post("/chat/completions")
async def chat_completions(
    request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    start_time = datetime.utcnow()

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    # Sprint 3: Policy Engine decides the exact model route based on metadata rules.
    original_model = payload.get("model", "unknown")
    routed_model = PolicyEngine.determine_route(payload)

    # Mutate the payload to force the remote LiteLLM to use the required model
    payload["_original_requested_model"] = (
        original_model  # store temporally to pass down
    )
    payload["model"] = routed_model

    target_url = f"{settings.LITELLM_API_BASE.rstrip('/')}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.LITELLM_API_KEY}",
        "Content-Type": "application/json",
    }

    current_model = routed_model
    max_attempts = 3
    attempts = 0
    last_error_detail = ""
    last_status_code = 502

    async with httpx.AsyncClient() as client:
        while attempts < max_attempts:
            attempts += 1
            payload["model"] = current_model

            try:
                response = await client.post(
                    target_url, json=payload, headers=headers, timeout=60.0
                )
                latency_ms = int(
                    (datetime.utcnow() - start_time).total_seconds() * 1000
                )

                if response.status_code == 200:
                    resp_json = response.json()
                    status_msg = "success"
                    if attempts > 1:
                        status_msg = f"success (fallback to {current_model})"

                    background_tasks.add_task(
                        log_transaction_to_db,
                        db=db,
                        request_data=payload,
                        response_data=resp_json,
                        status=status_msg,
                        latency_ms=latency_ms,
                    )
                    return resp_json
                else:
                    error_body = response.text
                    last_status_code = response.status_code
                    last_error_detail = error_body

                    status_str = f"failed (upstream {response.status_code})"
                    background_tasks.add_task(
                        log_transaction_to_db,
                        db=db,
                        request_data=payload,
                        response_data=None,
                        status=status_str,
                        latency_ms=latency_ms,
                        error_msg=error_body,
                    )

            except httpx.RequestError as e:
                latency_ms = int(
                    (datetime.utcnow() - start_time).total_seconds() * 1000
                )
                last_error_detail = str(e)
                last_status_code = 502
                background_tasks.add_task(
                    log_transaction_to_db,
                    db=db,
                    request_data=payload,
                    response_data=None,
                    status="failed (connection)",
                    latency_ms=latency_ms,
                    error_msg=last_error_detail,
                )

            # If we reached here, the attempt failed. Try to get a fallback model.
            fallback_model = PolicyEngine.get_fallback_model(current_model)
            if not fallback_model:
                break  # No fallback available, give up

            current_model = fallback_model

    # If we exit the loop without returning, all attempts/fallbacks failed
    return JSONResponse(
        status_code=last_status_code,
        content={
            "detail": f"LiteLLM Error (after {attempts} attempts): {last_error_detail}"
        },
    )
