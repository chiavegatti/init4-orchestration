import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.config import settings

client = TestClient(app)

def test_chat_completions_missing_auth():
    payload = {
        "model": "auto",
        "messages": [{"role": "user", "content": "Hello"}],
    }
    response = client.post("/v1/chat/completions", json=payload)
    assert response.status_code == 401
    assert "Missing Authorization header" in response.json()["detail"]

def test_chat_completions_invalid_auth():
    payload = {
        "model": "auto",
        "messages": [{"role": "user", "content": "Hello"}],
    }
    response = client.post(
        "/v1/chat/completions",
        json=payload,
        headers={"Authorization": "Bearer invalid-key"}
    )
    assert response.status_code == 401
    assert "Invalid service API Key" in response.json()["detail"]

def test_metrics_summary_missing_auth():
    response = client.get("/v1/metrics/summary")
    assert response.status_code == 401
    assert "Missing Authorization header" in response.json()["detail"]

def test_metrics_summary_invalid_auth():
    response = client.get(
        "/v1/metrics/summary",
        headers={"Authorization": "Bearer invalid-key"}
    )
    assert response.status_code == 401
    assert "Invalid admin API Key" in response.json()["detail"]
