from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from src.core.config import settings
from starlette.status import HTTP_401_UNAUTHORIZED

# Token headers definitions
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

async def verify_service_api_key(api_key: str = Depends(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )
    # Check if format is "Bearer token"
    if api_key.startswith("Bearer "):
        token = api_key.split(" ")[1]
    else:
        token = api_key

    if token != settings.SERVICE_API_KEY:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid service API Key",
        )
    return token

async def verify_admin_api_key(api_key: str = Depends(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )
    if api_key.startswith("Bearer "):
        token = api_key.split(" ")[1]
    else:
        token = api_key

    if token != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid admin API Key",
        )
    return token
