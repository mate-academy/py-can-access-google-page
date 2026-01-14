from unittest.mock import patch
from app import main


def test_can_access_google_page_accessible() -> None:
    """Test when internet is available and URL is valid."""
    with patch.object(main, "valid_google_url", return_value=True), \
         patch.object(main, "has_internet_connection", return_value=True):
        result = main.can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    """Test when there is no internet connection."""
    with patch.object(main, "valid_google_url", return_value=True), \
         patch.object(main, "has_internet_connection", return_value=False):
        result = main.can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    """Test when URL is invalid."""
    with patch.object(main, "valid_google_url", return_value=False), \
         patch.object(main, "has_internet_connection", return_value=True):
        result = main.can_access_google_page("https://wrong-url.com")
        assert result == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url() -> None:
    """Test when both URL is invalid and there is no internet."""
    with patch.object(main, "valid_google_url", return_value=False), \
         patch.object(main, "has_internet_connection", return_value=False):
        result = main.can_access_google_page("https://wrong-url.com")
        assert result == "Not accessible"
