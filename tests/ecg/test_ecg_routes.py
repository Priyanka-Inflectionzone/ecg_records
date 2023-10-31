import pytest
from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app instance

# Define your test data here
test_data = {
    "dirName": "apnea-ecg/",
    "recordName": "a01",
    "extension": "apn",
}

@pytest.fixture
def client():
    return TestClient(app)

def test_read_ecg(client):
    response = client.post("/read-ecg-data", json=test_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Record Converted Successfully"