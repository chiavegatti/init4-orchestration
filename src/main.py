from fastapi import FastAPI

app = FastAPI(
    title="INIT4 Cognitive Orchestrator",
    description="Deterministic AI request orchestrator and proxy via LiteLLM.",
    version="1.0.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "orchestrator"}
