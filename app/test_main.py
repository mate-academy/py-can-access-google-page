from unittest.mock import patch
# Assuming can_access_google_page is in main.py within the app folder
from app.main import can_access_google_page 

# Example test for the first scenario
def test_can_access_google_page_accessible():
    with patch('app.main.valid_google_url', return_value=True), \
         patch('app.main.has_internet_connection', return_value=True):
        assert can_access_google_page("https://google.com") == "Accessible"

