from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible():
    url = "https://www.google.com"
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page(url) == "Accessible", "Expected 'Accessible' when both conditions are True"


def test_can_access_google_page_invalid_url():
    url = "https://www.invalid-url.com"
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page(url) == "Not accessible", "Expected 'Not accessible' when URL is invalid"


def test_can_access_google_page_no_internet():
    url = "https://www.google.com"
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page(url) == "Not accessible", "Expected 'Not accessible' when no internet connection"


def test_can_access_google_page_not_accessible():
    url = "https://www.invalid-url.com"
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page(url) == "Not accessible", "Expected 'Not accessible' when both conditions are False"
