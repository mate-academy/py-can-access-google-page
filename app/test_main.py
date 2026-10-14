from unittest import mock
from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Accessible"


def test_valid_url_and_invalid_connection() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False):
        with mock.patch("app.main.valid_google_url", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_invalid_url_and_valid_connection_exists() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=False):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_invalid_url_and_invalid_connection() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False):
        with mock.patch("app.main.valid_google_url", return_value=False):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"
