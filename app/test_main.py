from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_connection, mock_valid_url):
    mock_valid_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mock_valid_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.invalid-url.com") == "Not accessible"

    mock_valid_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.invalid-url.com") == "Not accessible"
