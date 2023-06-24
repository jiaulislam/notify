from fastapi import status
from fastapi.testclient import TestClient

from notify import app

client = TestClient(app)


def test_healthcheck_aliveness():
    response = client.get("/api/v1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["apiStatus"] == "alive"
