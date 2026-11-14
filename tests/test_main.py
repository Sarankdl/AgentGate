from fastapi.testclient import TestClient

from agentgate.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_echo():
    response = client.post("/echo", json={"hello": "world"})
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
