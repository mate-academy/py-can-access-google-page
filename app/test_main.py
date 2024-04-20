from unittest import mock
from app.main import can_access_google_page


def test_valid_url_and_has_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True), \
            mock.patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_valid_url_but_no_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True), \
            mock.patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_not_valid_url_but_has_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False), \
            mock.patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_not_valid_url_and_no_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False), \
            mock.patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
