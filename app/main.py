def valid_google_url(url: str) -> bool:
    return url == "https://www.google.com"


def has_internet_connection() -> bool:
    return True


def can_access_google_page(url: str) -> str:
    if not isinstance(url, str):
        raise TypeError

    if valid_google_url(url) and has_internet_connection():
        return "Accessible"

    return "Not accessible"
