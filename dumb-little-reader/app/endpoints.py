from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.models import Feed, Item, Reaction
from app.rss_fetcher import fetch_rss_feed, parse_rss_feed

app = FastAPI()

feeds = []


@app.post("/subscribe")
async def subscribe_feed(url: str):
    try:
        rss_feed = fetch_rss_feed(url)
        feed = parse_rss_feed(rss_feed)
        feeds.append(feed)
        return {"success": True, "message": "Subscribed to feed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/items", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10):
    items = [item for feed in feeds for item in feed.items]
    return items[skip : skip + limit]


@app.post("/mark-as-read")
async def mark_item_as_read(item_id: str):
    for feed in feeds:
        for item in feed.items:
            if item.id == item_id:
                item.read = True
                return {"success": True, "message": "Item marked as read"}

    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/react-to-item")
async def react_to_item(item_id: str, reaction: Reaction):
    for feed in feeds:
        for item in feed.items:
            if item.id == item_id:
                item.reaction = reaction
                return {"success": True, "message": "Reaction added"}

    raise HTTPException(status_code=404, detail="Item not found")