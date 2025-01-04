from unittest.mock import patch
import pytest
from main import can_access_google_page

@patch("main.valid_google_url")
@patch("main.has_internet_connection")
def test_valid_url_and_connection_exists(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

@patch("main.valid_google_url")
@patch("main.has_internet_connection")
def test_invalid_url(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.invalid-url.com")
    assert result == "Not accessible"

@patch("main.valid_google_url")
@patch("main.has_internet_connection")
def test_no_internet_connection(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


if __name__ == "__main__":
    pytest.main()
