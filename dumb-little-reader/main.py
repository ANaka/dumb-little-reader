from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from app.rss_fetcher import fetch_rss_feed, get_feed_items
from app.models import Feed, FeedItem, Reaction
from app.endpoints import add_feed, get_feed_items, mark_as_read, set_reaction

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/feeds")
async def subscribe(feed_url: str):
    try:
        return await add_feed(feed_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/feeds/{feed_id}/items", response_model=List[FeedItem])
async def get_items(feed_id: int, skip: int = 0, limit: int = 10):
    try:
        return await get_feed_items(feed_id, skip, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/items/{item_id}/read")
async def mark_item_as_read(item_id: int):
    try:
        return await mark_as_read(item_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/items/{item_id}/reaction")
async def set_item_reaction(item_id: int, reaction: Reaction):
    try:
        return await set_reaction(item_id, reaction)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))