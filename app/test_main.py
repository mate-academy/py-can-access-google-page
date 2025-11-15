from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_with_valid_url_and_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"


def test_can_access_google_page_when_no_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=False):
        with patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_can_access_google_page_when_url_invalid() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("https://youtube.com")
            assert result == "Not accessible"
