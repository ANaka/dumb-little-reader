import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.error_handling import handle_invalid_url, handle_failed_request

client = TestClient(app)

def test_handle_invalid_url():
    invalid_url = "not-a-valid-url"
    with pytest.raises(ValueError) as exc_info:
        handle_invalid_url(invalid_url)
    assert str(exc_info.value) == f"Invalid URL: {invalid_url}"

def test_handle_failed_request():
    failed_url = "http://nonexistent-url.com/rss"
    with pytest.raises(Exception) as exc_info:
        handle_failed_request(failed_url)
    assert str(exc_info.value) == f"Failed to fetch RSS feed from: {failed_url}"

def test_error_handling_invalid_url():
    response = client.post("/subscribe", json={"url": "not-a-valid-url"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid URL: not-a-valid-url"}

def test_error_handling_failed_request():
    response = client.post("/subscribe", json={"url": "http://nonexistent-url.com/rss"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to fetch RSS feed from: http://nonexistent-url.com/rss"}