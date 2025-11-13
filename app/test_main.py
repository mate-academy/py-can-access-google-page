from unittest.mock import patch
from app.main import can_access_google_page

def test_can_access_google_page_accessible():
    with patch("app.main.valid_google_url") as mock_valid_url, \
         patch("app.main.has_internet_connection") as mock_internet:
        mock_valid_url.return_value = True
        mock_internet.return_value = True

        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"

def test_can_access_google_page_not_accessible_invalid_url():
    with patch("app.main.valid_google_url") as mock_valid_url, \
         patch("app.main.has_internet_connection") as mock_internet:
        mock_valid_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"

def test_can_access_google_page_not_accessible_no_internet():
    with patch("app.main.valid_google_url") as mock_valid_url, \
         patch("app.main.has_internet_connection") as mock_internet:
        mock_valid_url.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

def test_can_access_google_page_not_accessible_both_false():
    with patch("app.main.valid_google_url") as mock_valid_url, \
         patch("app.main.has_internet_connection") as mock_internet:
        mock_valid_url.return_value = False
        mock_internet.return_value = False

        result = can_access_google_page("https://invalid-url.com")
        assert result == "Not accessible"
