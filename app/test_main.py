from unittest.mock import patch
from main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_can_access_google_page_not_accessible_both_fail() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"
