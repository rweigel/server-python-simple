from fastapi.testclient import TestClient

from .hapi import app

client = TestClient(app)

def test_read_main():
    response = client.get("/data/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}