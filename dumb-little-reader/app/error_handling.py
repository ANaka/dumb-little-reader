from fastapi import HTTPException

class InvalidRSSFeedError(HTTPException):
    def __init__(self, url: str):
        super().__init__(status_code=400, detail=f"Invalid RSS feed URL: {url}")

class FetchRSSFeedError(HTTPException):
    def __init__(self, url: str):
        super().__init__(status_code=500, detail=f"Failed to fetch RSS feed from URL: {url}")

class ItemNotFoundError(HTTPException):
    def __init__(self, item_id: str):
        super().__init__(status_code=404, detail=f"Item not found with ID: {item_id}")

class FeedNotFoundError(HTTPException):
    def __init__(self, feed_id: str):
        super().__init__(status_code=404, detail=f"Feed not found with ID: {feed_id}")