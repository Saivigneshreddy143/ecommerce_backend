from fastapi import FastAPI

from ecommerce_backend.api.v1.router import api_router
from ecommerce_backend.core.config import settings


def create_application() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Backend API for the multi-vendor marketplace.",
        debug=settings.debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    application.include_router(api_router, prefix=settings.api_v1_prefix)

    @application.get("/", tags=["Root"], summary="Service Root")
    async def root() -> dict[str, str]:
        """Return basic service info and API documentation links."""
        return {
            "service": settings.app_name,
            "version": settings.app_version,
            "docs": "/docs",
            "health": f"{settings.api_v1_prefix}/health",
        }

    return application


app = create_application()