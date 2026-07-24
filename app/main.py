import datetime

import requests


def valid_google_url(url: str) -> bool:
    return requests.get(url).status_code == 200


def has_internet_connection() -> bool:
    return 6 <= datetime.datetime.now().hour < 23


def can_access_google_page(url: str) -> str:
    if valid_google_url(url) and has_internet_connection():
        return "Accessible"
    return "Not accessible"
