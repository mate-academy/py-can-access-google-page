from unittest.mock import patch
from app.main import can_access_google_page


def test_returns_accessible_when_both_true() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_returns_not_accessible_when_both_false() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_returns_not_accessible_if_only_connection_true() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_returns_not_accessible_if_only_valid_url_true() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
