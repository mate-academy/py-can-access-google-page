from unittest.mock import patch
from app.main import can_access_google_page


def test_can_accessible_when_valid_url_and_internet_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_when_invalid_url() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page(
            "https://invalid-url.com"
        ) == "Not accessible"


def test_not_accessible_when_no_internet_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_not_accessible_when_invalid_url_and_no_internet() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page(
            "https://invalid-url.com"
        ) == "Not accessible"
