from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Accessible"


def test_if_only_internet_connection_is_true() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True):
        with mock.patch("app.main.valid_google_url", return_value=False):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_if_only_valid_google_url_is_true() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False):
        with mock.patch("app.main.valid_google_url", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"
