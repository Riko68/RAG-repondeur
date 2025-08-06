from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint returns correct response."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_health_check_method_not_allowed():
    """Test health check endpoint rejects POST requests."""
    response = client.post("/health")
    assert response.status_code == 405

def test_nonexistent_endpoint():
    """Test accessing a non-existent endpoint returns 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404