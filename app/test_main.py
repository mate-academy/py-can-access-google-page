from unittest.mock import patch

from app.main import can_access_google_page


def test_can_access_when_valid_url_and_internet() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
            patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_when_valid_url_and_not_internet() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
            patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_when_not_valid_url_and_valid_internet_connection() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
            patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_when_has_valid_url_and_internet_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
            patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"
