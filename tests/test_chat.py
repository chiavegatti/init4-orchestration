import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock, MagicMock
from src.main import app
from src.db.session import get_db

client = TestClient(app)

# Mocks moved to conftest.py

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test-service-key"}

@pytest.mark.asyncio
def test_chat_completions_success(auth_headers):
    payload = {
        "model": "auto",
        "messages": [{"role": "user", "content": "Extract data"}],
        "metadata": {"task_type": "extraction"}
    }
    
    mock_post = AsyncMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": "chatcmpl-123",
        "model": "gpt-4o-mini",
        "choices": [{"message": {"content": "Data extracted"}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5}
    }
    mock_post.return_value = mock_response

    with patch('src.api.v1.chat.httpx.AsyncClient.post', mock_post):
        response = client.post("/v1/chat/completions", json=payload, headers=auth_headers)
        
    assert response.status_code == 200
    assert response.json()["id"] == "chatcmpl-123"

@pytest.mark.asyncio
def test_chat_completions_fallback(auth_headers):
    payload = {
        "model": "auto",
        "metadata": {"task_type": "extraction", "force_local": True}
    }
    
    # First request fails, second (fallback) succeeds
    mock_post = AsyncMock()
    
    mock_response_fail = MagicMock()
    mock_response_fail.status_code = 502
    mock_response_fail.text = "Bad Gateway"
    
    mock_response_success = MagicMock()
    mock_response_success.status_code = 200
    mock_response_success.json.return_value = {"id": "chatcmpl-fallback"}
    
    mock_post.side_effect = [mock_response_fail, mock_response_success]

    with patch('src.api.v1.chat.httpx.AsyncClient.post', mock_post):
        response = client.post("/v1/chat/completions", json=payload, headers=auth_headers)
        
    assert response.status_code == 200
    assert response.json()["id"] == "chatcmpl-fallback"
    assert mock_post.call_count == 2

@pytest.mark.asyncio
def test_chat_completions_all_fail(auth_headers):
    payload = {
        "model": "auto",
        "metadata": {"task_type": "unknown"}
    }
    
    mock_post = AsyncMock()
    mock_response_fail = MagicMock()
    mock_response_fail.status_code = 502
    mock_response_fail.text = "Bad Gateway"
    
    mock_post.side_effect = [mock_response_fail, mock_response_fail, mock_response_fail]

    with patch('src.api.v1.chat.httpx.AsyncClient.post', mock_post):
        response = client.post("/v1/chat/completions", json=payload, headers=auth_headers)
        
    assert response.status_code == 502
    assert "LiteLLM Error" in response.json()["detail"]

@pytest.mark.asyncio
def test_chat_completions_connection_error(auth_headers):
    payload = {
        "model": "auto",
        "metadata": {"task_type": "extraction"}
    }
    
    import httpx
    
    mock_post = AsyncMock()
    mock_post.side_effect = httpx.RequestError("Connection timeout")

    with patch('src.api.v1.chat.httpx.AsyncClient.post', mock_post):
        response = client.post("/v1/chat/completions", json=payload, headers=auth_headers)
        
    assert response.status_code == 502
    assert "Connection timeout" in response.json()["detail"]

def test_chat_completions_invalid_json(auth_headers):
    response = client.post("/v1/chat/completions", data="invalid json", headers=auth_headers)
    assert response.status_code == 400
    # Wait, invalid json might be caught by FastAPI standard request.json() exception, which raises 400.
    
