import pytest
from app.rss_fetcher import fetch_rss_feed, parse_rss_feed

def test_fetch_rss_feed():
    url = "https://www.example.com/rss"
    response = fetch_rss_feed(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/rss+xml"

def test_fetch_rss_feed_invalid_url():
    url = "https://www.invalid-url.com/rss"
    with pytest.raises(Exception):
        fetch_rss_feed(url)

def test_parse_rss_feed():
    rss_xml = """
    <rss version="2.0">
        <channel>
            <title>Example RSS Feed</title>
            <item>
                <title>Example Item 1</title>
                <link>https://www.example.com/item1</link>
                <pubDate>Mon, 01 Jan 2022 00:00:00 GMT</pubDate>
            </item>
            <item>
                <title>Example Item 2</title>
                <link>https://www.example.com/item2</link>
                <pubDate>Tue, 02 Jan 2022 00:00:00 GMT</pubDate>
            </item>
        </channel>
    </rss>
    """
    feed, items = parse_rss_feed(rss_xml)
    assert feed.title == "Example RSS Feed"
    assert len(items) == 2
    assert items[0].title == "Example Item 1"
    assert items[0].link == "https://www.example.com/item1"
    assert items[1].title == "Example Item 2"
    assert items[1].link == "https://www.example.com/item2"

def test_parse_rss_feed_invalid_xml():
    invalid_rss_xml = "<rss><channel></rss>"
    with pytest.raises(Exception):
        parse_rss_feed(invalid_rss_xml)