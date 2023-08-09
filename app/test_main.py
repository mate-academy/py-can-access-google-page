from app.main import (
    can_access_google_page,
    valid_google_url,
    has_internet_connection
)


def test_cannot_access_if_connection_or_valid_url_is_true() -> None:
    url = "http://google.com"
    result_connection = has_internet_connection()
    result_valid = valid_google_url(url)
    if result_connection and result_valid:
        assert can_access_google_page(url) == "Accessible"
    else:
        assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_if_only_connection() -> None:
    url = "http://google.com"
    result_connection = has_internet_connection()
    result_valid = valid_google_url(url)
    if result_connection and not result_valid:
        assert can_access_google_page(url) == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    url = "http://google.com"
    result_connection = has_internet_connection()
    result_valid = valid_google_url(url)
    if not result_connection and result_valid:
        assert can_access_google_page(url) == "Not accessible"
