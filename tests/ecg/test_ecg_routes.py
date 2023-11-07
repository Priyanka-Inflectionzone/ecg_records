import pytest
from app.startup.application import app
from tests.test_config import test_client

test_data = {
    "dirName": "apnea-ecg/",
    "recordName": "a01",
    "extension": "apn",
}

def test_read_ecg(test_client):
    response = test_client.post("/api/v1/ecg/read-ecg-data",
                                headers = { "Content-Type": "application/json"},
                                json=test_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Record Converted Successfully"