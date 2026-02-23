import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.session import get_db

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
    def add(self, *args, **kwargs):
        pass
    def commit(self):
        pass

def override_get_db():
    try:
        yield MockSession()
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def test_app():
    return app

@pytest.fixture
def client(test_app):
    return TestClient(test_app)
