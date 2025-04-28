from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with patch("app.test_main.valid_google_url", return_value=True), \
         patch("app.test_main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url() -> None:
    with patch("app.test_main.valid_google_url", return_value=False), \
         patch("app.test_main.has_internet_connection", return_value=True):
        result = can_access_google_page("invalid_url")
        assert result == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet() -> None:
    with patch("app.test_main.valid_google_url", return_value=True), \
         patch("app.test_main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
