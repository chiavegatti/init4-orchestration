from fastapi import FastAPI
from src.api.v1 import chat, metrics

app = FastAPI(
    title="INIT4 Cognitive Orchestrator",
    description="Deterministic AI request orchestrator and proxy via LiteLLM.",
    version="1.0.0",
)

app.include_router(chat.router, prefix="/v1", tags=["LLM Proxy"])
app.include_router(
    metrics.router, prefix="/v1/metrics", tags=["Metrics & Cost Dashboard"]
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "orchestrator"}
