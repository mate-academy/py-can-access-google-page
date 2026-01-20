import datetime
import requests
from urllib.parse import urlparse


def valid_google_url(url: str) -> bool:
    """
    Checks if the URL is a valid Google homepage URL.
    """
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc in ["www.google.com", "google.com"]:
            response = requests.get(url, timeout=3)
            return response.status_code == 200
        return False
    except requests.RequestException:
        return False  # Handles network issues, invalid URLs, etc.


def has_internet_connection() -> bool:
    """
    Returns True if the current time is between 6:00:00 and 22:59:59.
    """
    current_time = datetime.datetime.now()
    return 6 <= current_time.hour < 23


def can_access_google_page(url: str) \
        -> str:
    """
    Determines if the Google homepage is accessible
    based on internet connection and URL validity.
    """
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
