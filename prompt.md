# dumb-little-reader: a simple RSS feed reader

Specification:
- The user needs to be able to enter URLs in order to subscribe to RSS feeds.
- The application needs to store the subscribed RSS feeds.
- The application needs to fetch the latest items from the subscribed RSS feeds.
- The application needs to display the latest items from the subscribed RSS feeds.
- The application needs to allow the user to click on an item to view it in a new tab.
- The application needs to mark items as read when the user clicks on them.
- The application needs to allow the user to scroll down to load more items.
- The application needs to allow a user to mark an item as liked, loved, or disliked.

Components:
- AI developer documentation and roadmap. This is an AI-to-human communication channel. It should be a document that informs a human developer how to run tests and deploy the application. It should also include questions that the AI has about the application, and highlight areas that need further development and/or human code review.
- FastAPI Application: The application will be written in Python using the FastAPI framework due to its high performance, ease of use, automatic API documentation, and support for asynchronous programming.
- RSS Feed Fetching: The application will make HTTP requests to fetch RSS feeds from the provided URLs. This can be achieved using Python's httpclient or requests library. The fetched RSS feeds, being XML, will be parsed into a Python data structure for easier manipulation. Python's feedparser library can be used for this purpose.
- Hosting on Modal: The application will be hosted on Modal. This will involve creating a Modal account, installing the modal-client package, setting up a token, and then deploying the Python code to Modal​​.
- Web Endpoints: The application will define web endpoints to serve the RSS feed items. This can be done using the routing capabilities of FastAPI.
- User Interface: The application will provide a user interface for viewing RSS feed items. This interface will be built using HTML and CSS, and will include elements for displaying the feed items and handling user interactions like scrolling.
- Error Handling and Testing: The application will implement error handling to manage potential issues like failed HTTP requests or invalid RSS feed URLs. It will also include tests to ensure that each part of the application is working correctly. FastAPI makes it easy to write tests using pytest.
