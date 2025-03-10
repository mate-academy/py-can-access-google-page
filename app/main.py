import datetime
import requests


def valid_google_url(url: str) -> bool:
    response = requests.get(url)
    return response.status_code == 200


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return current_time.hour in range(6, 23)


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    else:
        return "Not accessible"
