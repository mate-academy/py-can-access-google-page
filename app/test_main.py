import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: any, mock_valid_google_url: any) -> None:

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True


    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
