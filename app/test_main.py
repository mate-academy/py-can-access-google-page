from unittest.mock import patch
from app.main import can_access_google_page

def test_accessible_when_url_valid_and_internet_available():
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("https://www.google.com") is True

def test_not_accessible_when_url_invalid():
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("invalid-url") is False

def test_not_accessible_when_no_internet():
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page("https://www.google.com") is False

def test_not_accessible_when_url_invalid_and_no_internet():
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page("invalid-url") is False
