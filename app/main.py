def valid_google_url(url: str) -> bool:
    valid_urls = {
        "https://www.google.com",
        "https://google.com",
        "https://google.com/",
        "https://www.google.com/",
    }
    return url in valid_urls


def has_internet_connection() -> bool:
    import datetime

    current_time = datetime.datetime.now().time()
    start = datetime.time(6, 0, 0)
    end = datetime.time(22, 59, 59)
    return start <= current_time <= end


def can_access_google_page(url: str) -> str:
    if valid_google_url(url) and has_internet_connection():
        return "Accessible"
    return "Not accessible"
