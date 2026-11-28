from datetime import datetime, timezone

from fastapi import APIRouter, status
from pydantic import BaseModel

from ecommerce_backend.core.config import settings

router = APIRouter()


class HealthResponse(BaseModel):
    """Response schema for the service health check."""

    status: str
    service: str
    version: str
    environment: str
    timestamp: datetime


@router.get(
    "",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Verify that the API service is running and responsive.",
)
async def health_check() -> HealthResponse:
    """Return service health status and metadata."""
    return HealthResponse(
        status="ok",
        service=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(timezone.utc),
    )