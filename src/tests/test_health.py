from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_healthcheck_status():
    response = client.get("/common/healthcheck")
    assert response.status_code == 200


def test_healthcheck_body():
    response = client.get("/common/healthcheck")
    data = response.json()
    assert data["status"] == "ok"


def test_unknown_route():
    response = client.get("/definitely-not-existing")
    assert response.status_code == 404
