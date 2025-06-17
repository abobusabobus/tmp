from fastapi.testclient import TestClient
from main import app
import uuid
client = TestClient(app)



def test_create_user():
    random_email = f"user_{uuid.uuid4()}@example.com"
    response = client.post("/users/", json={"name": "John Doe", "email": random_email})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == random_email


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
