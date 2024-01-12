from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: Callable,
    mock_valid_google_url: Callable
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mock_valid_google_url.return_value = False
    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
