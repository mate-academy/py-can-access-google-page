from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_with_valid_url_and_connection() -> None:
    """Accessible when both URL is valid and internet connection exists."""
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_without_connection() -> None:
    """Not accessible when URL is valid but no internet connection."""
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_not_accessible_with_invalid_url() -> None:
    """Not accessible when internet exists but URL is invalid."""
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_not_accessible_with_invalid_url_and_no_connection() -> None:
    """Not accessible when both URL is invalid and no internet connection."""
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )
