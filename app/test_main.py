from unittest.mock import patch
from app import main


def test_can_access_google_page_accessible():
    with patch.object(main, "valid_google_url", return_value=True), \
         patch.object(main, "has_internet_connection", return_value=True):
        result = main.can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_google_page_no_internet():
    with patch.object(main, "valid_google_url", return_value=True), \
         patch.object(main, "has_internet_connection", return_value=False):
        result = main.can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url():
    with patch.object(main, "valid_google_url", return_value=False), \
         patch.object(main, "has_internet_connection", return_value=True):
        result = main.can_access_google_page("https://wrong-url.com")
        assert result == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url():
    with patch.object(main, "valid_google_url", return_value=False), \
         patch.object(main, "has_internet_connection", return_value=False):
        result = main.can_access_google_page("https://wrong-url.com")
        assert result == "Not accessible"
