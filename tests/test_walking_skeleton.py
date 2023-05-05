from starlette.testclient import TestClient

from main import app


def test_read_main():
    client = TestClient(app)
    response = client.get("/walking_skeleton")
    assert response.status_code == 200
    assert response.json() == {"Walking": "Skeleton"}
