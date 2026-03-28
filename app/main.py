def valid_google_url(url: str) -> bool:
    return url in ["https://google.com", "https://www.google.com"]


def has_internet_connection() -> bool:
    from datetime import datetime, time

    now = datetime.now().time()
    start = time(6, 0, 0)
    end = time(22, 59, 59)

    return start <= now <= end


def can_access_google_page(url: str) -> str:
    if valid_google_url(url) and has_internet_connection():
        return "Accessible"
    return "Not accessible"
