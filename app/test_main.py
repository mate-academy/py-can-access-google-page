from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_success(mock_valid_url, mock_internet_connection):
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(mock_valid_url, mock_internet_connection):
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(mock_valid_url, mock_internet_connection):
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("invalid-url")
    assert result == "Not accessible"
