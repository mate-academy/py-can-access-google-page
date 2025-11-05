import datetime
import requests


def valid_google_url(url: str) -> bool:
    """Return True if URL is valid and accessible (status 200)."""
    response = requests.get(url)
    return response.status_code == 200


def has_internet_connection() -> bool:
    """Return True if current time is between 06:00 and 22:59."""
    current_time = datetime.datetime.now()
    return 6 <= current_time.hour < 23


def can_access_google_page(url: str) -> str:
    """
    Return 'Accessible' if both internet connection and URL are valid,
    else 'Not accessible'.
    """
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
