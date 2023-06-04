from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from .rss_fetcher import fetch_rss_feed, parse_rss_feed
from .models import Feed, Item, Reaction

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

subscribed_feeds: List[Feed] = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/subscribe")
async def subscribe_feed(url: str):
    rss_feed = fetch_rss_feed(url)
    if not rss_feed:
        raise HTTPException(status_code=400, detail="Invalid RSS feed URL")

    feed = parse_rss_feed(rss_feed)
    subscribed_feeds.append(feed)
    return {"success": True}


@app.get("/items")
async def get_items(offset: int = 0, limit: int = 10):
    items = [item for feed in subscribed_feeds for item in feed.items]
    items.sort(key=lambda x: x.published, reverse=True)
    return items[offset : offset + limit]


@app.post("/mark-as-read")
async def mark_item_as_read(item_id: str):
    for feed in subscribed_feeds:
        for item in feed.items:
            if item.id == item_id:
                item.read = True
                return {"success": True}
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/react-to-item")
async def react_to_item(item_id: str, reaction: Reaction):
    for feed in subscribed_feeds:
        for item in feed.items:
            if item.id == item_id:
                item.reaction = reaction
                return {"success": True}
    raise HTTPException(status_code=404, detail="Item not found")