from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_not_valid_google_url() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://fake.com")
        assert result == "Not accessible"


def test_not_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
