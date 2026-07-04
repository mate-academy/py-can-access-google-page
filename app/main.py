import datetime
import requests


def valid_google_url(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return current_time.hour in range(6, 23)


def can_access_google_page(url: str) -> str:
    if not has_internet_connection() or not valid_google_url(url):
        return "Not accessible"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "Accessible"
    except requests.RequestException:
        return "Not accessible"
    return "Not accessible"
