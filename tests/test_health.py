from fastapi.testclient import TestClient

from ecommerce_backend.main import app

client = TestClient(app)


def test_health_check_returns_200() -> None:
    """Health endpoint should respond with HTTP 200 and expected status payload."""
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data
    assert "version" in data
    assert "environment" in data
    assert "timestamp" in data


def test_swagger_docs_accessible() -> None:
    """Swagger UI and OpenAPI schema endpoints should be accessible."""
    docs_response = client.get("/docs")
    openapi_response = client.get("/openapi.json")

    assert docs_response.status_code == 200
    assert openapi_response.status_code == 200