import datetime
import requests


def valid_google_url(url: str) -> bool:
    response = requests.get(url)
    return True if response.status_code == 200 else False


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return True if current_time.hour in range(6, 23) else False


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    else:
        return "Not Accessible"
