from unittest.mock import patch
from app.main import can_access_google_page


valid_url = "https://www.google.com"


def test_can_access_google_page() -> None:
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=True)
    ):
        assert can_access_google_page(valid_url) == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url() -> None:
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=True)
    ):
        assert can_access_google_page(valid_url) == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet() -> None:
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=False)
    ):
        assert can_access_google_page(valid_url) == "Not accessible"


def test_can_access_google_page_not_accessible_both_fail() -> None:
    with (
        patch("app.main.valid_google_url", return_value=False),
        patch("app.main.has_internet_connection", return_value=False)
    ):
        assert can_access_google_page(valid_url) == "Not accessible"
