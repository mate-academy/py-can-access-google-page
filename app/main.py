import datetime


def valid_google_url(url: str) -> bool:
    valid_urls = (
        "https://google.com",
        "https://www.google.com",
    )
    return url in valid_urls


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return current_time.hour in range(6, 23)


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"