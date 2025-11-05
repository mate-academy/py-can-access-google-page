import pytest
from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_only_if_both_true():
    """Check page is accessible only if both URL is valid and internet exists."""
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert can_access_google_page("https://www.google.com") == "Accessible"

    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )

    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )

    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )


def test_not_accessible_if_only_one_condition_true():
    """Ensure function is NOT accessible if only one condition is True."""
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=False),
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible", (
            "Should not be accessible if only URL is valid."
        )

    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible", (
            "Should not be accessible if only internet works."
        )
