from unittest.mock import patch

from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"


def test_invalid_url_and_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_valid_url_and_lost_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
