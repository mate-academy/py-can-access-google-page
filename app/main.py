import datetime

import requests


def valid_google_url(url: str) -> bool:
    response = requests.get(url)
    return True if response.status_code == 200 else False  # noqa: SIM210


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return True if current_time.hour in range(6, 23) else False  # noqa: SIM210


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    else:
        return "Not accessible"
