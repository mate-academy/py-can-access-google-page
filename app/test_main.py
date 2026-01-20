from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_when_internet_and_url_valid() -> None:
    with patch("app.main.has_internet_connection", return_value=True), patch(
        "app.main.valid_google_url", return_value=True
    ):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_not_access_google_page_when_no_internet_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=False), patch(
        "app.main.valid_google_url", return_value=True
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_can_not_access_google_page_when_no_valid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True), patch(
        "app.main.valid_google_url", return_value=False
    ):
        assert (
            can_access_google_page("https://www.invalid-url.com")
            == "Not accessible"
        )


def test_can_not_access_when_no_internet_and_no_valid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), patch(
        "app.main.valid_google_url", return_value=False
    ):
        assert (
            can_access_google_page("https://www.invalid-url.com")
            == "Not accessible"
        )
