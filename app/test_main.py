from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


# Test cases for can_access_google_page function
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    # Test case 1: Both internet connection and URL are valid
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    # Test case 2: Internet connection is valid, but URL is invalid
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https:"
                                  "//www.invalidurl.com") == "Not accessible"

    # Test case 3: Internet connection is invalid, but URL is valid
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    # Test case 4: Both internet connection and URL are invalid
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://www."
                                  "invalidurl.com") == "Not accessible"
