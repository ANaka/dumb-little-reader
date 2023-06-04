import requests
import feedparser

def fetch_rss_feed(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_rss_feed(feed_content: str):
    parsed_feed = feedparser.parse(feed_content)
    return parsed_feed
