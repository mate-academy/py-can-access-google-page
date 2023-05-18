from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://www.google.com") == "Accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection",
                        return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_cannot_access_if_only_has_internet_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection",
                        return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_cannot_access_in_two_ways() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection",
                        return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
