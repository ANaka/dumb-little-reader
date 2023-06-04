# Dumb Little Reader

A simple RSS feed reader built with FastAPI, Python, and HTML/CSS.

## Features

- Subscribe to RSS feeds by entering URLs
- Store subscribed RSS feeds
- Fetch and display latest items from subscribed RSS feeds
- Click on an item to view it in a new tab
- Mark items as read when clicked
- Scroll down to load more items
- Mark items as liked, loved, or disliked

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/dumb-little-reader.git
```

2. Change to the project directory:

```
cd dumb-little-reader
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

1. Run the FastAPI application:

```
uvicorn app.main:app --reload
```

2. Open your browser and navigate to `http://localhost:8000`.

## Testing

To run the tests, execute the following command:

```
pytest app/tests
```

## Contributing

Please read the AI developer documentation in `docs/ai_developer_documentation.md` and the project roadmap in `docs/roadmap.md` before contributing.

## License

This project is licensed under the MIT License.