from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_when_url_and_has_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_not_accessible_when_url_invalid() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.invalid.com")
        assert result == "Not accessible"


def test_not_accessible_when_no_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
