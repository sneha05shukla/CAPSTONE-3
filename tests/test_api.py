from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_health():

    response = client.get("/health")

    assert response.status_code == 200


def test_feedback():

    response = client.post(
        "/feedback",
        json={
            "query": "refund issue",
            "feedback": "thumbs_up"
        }
    )

    assert response.status_code == 200