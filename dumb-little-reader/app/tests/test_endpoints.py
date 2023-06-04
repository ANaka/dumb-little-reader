from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.models import Feed, Item
from app.rss_fetcher import fetch_rss_feed, parse_rss_feed

client = TestClient(app)

@pytest.fixture
def sample_feed():
    url = "https://example.com/rss"
    rss_feed = fetch_rss_feed(url)
    feed = parse_rss_feed(rss_feed)
    return feed

def test_subscribe_feed(sample_feed):
    response = client.post("/subscribe", json={"url": "https://example.com/rss"})
    assert response.status_code == 200
    assert response.json() == {"feed": sample_feed.dict()}

def test_get_items(sample_feed):
    client.post("/subscribe", json={"url": "https://example.com/rss"})
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": [item.dict() for item in sample_feed.items]}

def test_mark_item_as_read(sample_feed):
    client.post("/subscribe", json={"url": "https://example.com/rss"})
    item_id = sample_feed.items[0].id
    response = client.post("/mark-as-read", json={"item_id": item_id})
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "status": "read"}

def test_react_to_item(sample_feed):
    client.post("/subscribe", json={"url": "https://example.com/rss"})
    item_id = sample_feed.items[0].id
    reaction = "liked"
    response = client.post("/react", json={"item_id": item_id, "reaction": reaction})
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "reaction": reaction}