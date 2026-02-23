import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.session import get_db

client = TestClient(app)

# Mocks moved to conftest.py

def test_get_metrics_summary():
    response = client.get("/v1/metrics/summary", headers={"Authorization": "Bearer test-admin-key"})
    assert response.status_code == 200
    data = response.json()
    assert "total_requests" in data
    assert "total_cost_usd" in data
    assert "local_fallback_count" in data
    assert "average_latency_ms" in data

def test_get_metrics_requests():
    response = client.get("/v1/metrics/requests?limit=10&offset=0", headers={"Authorization": "Bearer test-admin-key"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
