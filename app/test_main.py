from app.main import can_access_google_page
from unittest import mock


def test_can_access_when_url_and_connection_are_valid() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=True),
        mock.patch("app.main.has_internet_connection", return_value=True)
    ):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_cannot_access_when_no_connection() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=True),
        mock.patch("app.main.has_internet_connection", return_value=False)
    ):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_cannot_access_when_invalid_url() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=False),
        mock.patch("app.main.has_internet_connection", return_value=True)
    ):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"


def test_cannot_access_when_no_connection_and_invalid_url() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=False),
        mock.patch("app.main.has_internet_connection", return_value=False)
    ):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"
