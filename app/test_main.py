from unittest.mock import patch
from app.main import can_access_google_page

@patch('app.main.valid_google_url')
@patch('app.main.has_internet_connection')
def test_can_access_google_page(mock_has_internet_connection, mock_valid_google_url):
    # Mocking the functions
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    # Test the function with a valid URL and internet connection
    assert can_access_google_page("https://www.google.com") == "Accessible"

    # Test the function with an invalid URL
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://www.invalidurl.com") == "Not accessible"

    # Test the function without internet connection
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

