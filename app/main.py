import datetime


def valid_google_url(url: str) -> bool:
    return url == "https://www.google.com"


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(6, 0, 0)
    end_time = datetime.time(22, 59, 59)
    return start_time <= current_time <= end_time


def can_access_google_page(url: str) -> str:
    if valid_google_url(url) and has_internet_connection():
        return "Accessible"

    return "Not accessible"
