import requests
import datetime


def valid_google_url(url: str) -> bool:
    response = requests.get(url)
    return response.status_code == 200


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return 6 <= current_time.hour < 23


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
