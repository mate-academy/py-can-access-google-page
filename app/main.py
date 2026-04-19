import datetime


def valid_google_url(url: str) -> bool:
    valid_urls = [
        "https://www.google.com",
        "https://google.com",
        "www.google.com",
        "google.com"
    ]
    return url in valid_urls


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return 6 <= current_time.hour < 23


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
