
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": True}

def test_create_account():
    account = {
        "name": "Ayush",
        "description": "Test",
        "balance": 100,
        "active": True
    }
    response = client.put("/accounts/1", json=account)
    assert response.status_code == 201

def test_get_account():
    response = client.get("/accounts/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Ayush"

def test_delete_account_fail():
    response = client.delete("/accounts/2")
    assert response.status_code == 422  
