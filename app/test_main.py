from unittest.mock import patch

from app.main import can_access_google_page


# Test function for can_access_google_page
def test_can_access_google_page() -> None:
    url = "https://www.google.com"

    # Case 1: Internet connection available and valid Google URL
    with patch("app.has_internet_connection", return_value=True), \
         patch("app.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"

    # Case 2: No internet connection but valid Google URL
    with patch("app.has_internet_connection", return_value=False), \
         patch("app.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"

    # Case 3: Internet connection available but invalid Google URL
    with patch("app.has_internet_connection", return_value=True), \
         patch("app.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"

    # Case 4: No internet connection and invalid Google URL
    with patch("app.has_internet_connection", return_value=False), \
         patch("app.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"
