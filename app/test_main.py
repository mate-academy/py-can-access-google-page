import datetime
from unittest.mock import patch
# Assuming can_access_google_page is in main.py within the app folder
from app.main import can_access_google_page 
from unittest.mock import patch



# Example of a corrected test case
def test_cannot_access_if_only_valid_url(monkeypatch):
    with patch('app.main.valid_google_url', return_value=True), \
         patch('app.main.has_internet_connection', return_value=False):
        # Directly test the behavior of `can_access_google_page`
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible", "You cannot access page if only 'valid url' is True but no internet connection."

# Corrected test function
def test_cannot_access_if_only_connection():
    with patch('app.main.valid_google_url', return_value=False), \
         patch('app.main.has_internet_connection', return_value=True):
        # Directly test the behavior of `can_access_google_page`
        result = can_access_google_page("https://notgoogle.com")
        assert result == "Not accessible", "You cannot access the page if there's an internet connection but the URL is not valid."


