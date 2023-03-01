from unittest.mock import patch
import app.main as main


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_access_allowed(mock_has_internet, mock_valid_google_url):
    assert main.can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_url_invalid(mock_has_internet, mock_valid_google_url):
    assert main.can_access_google_page("https://www.invalidurl.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_internet_unavailable(mock_has_internet, mock_valid_google_url):
    assert main.can_access_google_page("https://www.google.com") == "Not accessible"
