from typing import Callable
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    # Mock the return values of valid_google_url and has_internet_connection
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    # Call the can_access_google_page function with a valid URL
    result = can_access_google_page("https://www.google.com")

    # Assert that the result is "Accessible"
    assert result == "Accessible"

    # Reset the mock calls
    mock_valid_google_url.reset_mock()
    mock_has_internet_connection.reset_mock()

    # Mock the return values of valid_google_url and
    # has_internet_connection for an invalid URL
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    # Call the can_access_google_page function with an invalid URL
    result = can_access_google_page("https://invalid-url.com")

    # Assert that the result is "Not accessible" due to an invalid URL
    assert result == "Not accessible"

    # Reset the mock calls
    mock_valid_google_url.reset_mock()
    mock_has_internet_connection.reset_mock()

    # Mock the return values of valid_google_url and
    # has_internet_connection for a valid URL but no internet connection
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    # Call the can_access_google_page function
    # with a valid URL but no internet connection
    result = can_access_google_page("https://www.google.com")

    # Assert that the result is "Not accessible" due to no internet connection
    assert result == "Not accessible"
