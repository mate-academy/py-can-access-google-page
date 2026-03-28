from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_page_when_url_is_valid_and_connection_exists() -> None:
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert can_access_google_page("google.com") == "Accessible"


def test_if_url_is_invalid_and_connection_exists() -> None:
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert can_access_google_page("google.com") == "Not accessible"


def test_if_url_is_valid_and_connection_missing() -> None:
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert can_access_google_page("google.com") == "Not accessible"


def test_if_url_is_invalid_and_connection_missing() -> None:
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert can_access_google_page("google.com") == "Not accessible"
