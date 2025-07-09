from app.main import can_access_google_page
from unittest.mock import patch


def test_can_accessible_when_url_valid_and_internet_available():
    with patch('app.main.valid_google_url', return_value=True), \
         patch('app.main.has_internet_connection', return_value=True):
        assert can_access_google_page("https://www.google.com") == "Accessible"

def test_not_accessible_when_url_invalid():
    with patch('app.main.valid_google_url', return_value=False), \
         patch('app.main.has_internet_connection', return_value=True):
        assert can_access_google_page("invalid-url") == "Not accessible"

def test_not_accessible_when_internet_unavailable():
    with patch('app.main.valid_google_url', return_value=True), \
         patch('app.main.has_internet_connection', return_value=False):
        assert can_access_google_page("https://www.google.com") == "Not accessible"

def test_not_accessible_when_both_invalid():
    with patch('app.main.valid_google_url', return_value=False), \
         patch('app.main.has_internet_connection', return_value=False):
        assert can_access_google_page("invalid-url") == "Not accessible"
