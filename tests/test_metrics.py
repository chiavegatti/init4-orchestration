import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.session import get_db

client = TestClient(app)

# Create a mock session
class MockQuery:
    def __init__(self, data=None):
        self.data = data or []
    def count(self):
        return len(self.data)
    def scalar(self):
        return 0.0
    def filter(self, *args, **kwargs):
        return self
    def order_by(self, *args, **kwargs):
        return self
    def offset(self, *args, **kwargs):
        return self
    def limit(self, *args, **kwargs):
        return self
    def all(self):
        return self.data

class MockSession:
    def query(self, *args, **kwargs):
        return MockQuery()

def override_get_db():
    try:
        yield MockSession()
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db

def test_get_metrics_summary():
    response = client.get("/v1/metrics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_requests" in data
    assert "total_cost_usd" in data
    assert "local_fallback_count" in data
    assert "average_latency_ms" in data

def test_get_metrics_requests():
    response = client.get("/v1/metrics/requests?limit=10&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
