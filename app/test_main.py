from app.main import can_access_google_page
from unittest.mock import patch


def test_valid_url_and_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_valid_url_no_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_invalid_url_and_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://bad.com")
        assert result == "Not accessible"


def test_invalid_url_no_connection() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://bad.com")
        assert result == "Not accessible"
