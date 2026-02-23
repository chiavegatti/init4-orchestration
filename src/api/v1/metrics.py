from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from src.db.session import get_db
from src.models.request import RequestLog

router = APIRouter()


@router.get("/summary")
def get_metrics_summary(db: Session = Depends(get_db)):
    """
    Returns aggregated usage and cost statistics for a given time period or tenant.
    """
    total_requests = db.query(RequestLog).count()
    total_cost = db.query(func.sum(RequestLog.estimated_cost)).scalar() or 0.0

    # Calculate average latency
    average_latency = db.query(func.avg(RequestLog.latency_ms)).scalar() or 0.0

    # Calculate fallback count
    fallback_count = db.query(RequestLog).filter(RequestLog.status == "fallback_used").count()

    return {
        "total_requests": total_requests,
        "total_cost_usd": float(total_cost),
        "local_fallback_count": fallback_count,
        "average_latency_ms": int(average_latency),
    }

@router.get("/requests")
def get_metrics_requests(
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    tenant_id: Optional[str] = None,
    task_type: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Returns a paginated list of individual request logs for auditing.
    """
    query = db.query(RequestLog)
    
    if tenant_id:
        query = query.filter(RequestLog.tenant_id == tenant_id)
        
    if task_type:
        query = query.filter(RequestLog.task_type == task_type)
        
    requests = query.order_by(RequestLog.timestamp.desc()).offset(offset).limit(limit).all()
    
    return [
        {
            "id": str(r.id),
            "timestamp": r.timestamp.isoformat(),
            "tenant_id": r.tenant_id,
            "task_type": r.task_type,
            "requested_model": r.requested_model,
            "routed_model": r.routed_model,
            "input_tokens": r.input_tokens,
            "output_tokens": r.output_tokens,
            "estimated_cost": float(r.estimated_cost),
            "latency_ms": r.latency_ms,
            "status": r.status,
            "error_message": r.error_message
        }
        for r in requests
    ]
