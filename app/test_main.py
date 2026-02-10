from app.main import can_access_google_page
from unittest.mock import patch


def test_accessible_when_internet_and_valid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
        patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_accessible_when_internet_and_invalid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):

        result = can_access_google_page("https://www.fake-google.com")
        assert result == "Not accessible"


def test_accessible_when_no_internet_and_valid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_accessible_when_no_internet_and_invalid_google_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):

        result = can_access_google_page("https://www.fake-google.com")
        assert result == "Not accessible"
