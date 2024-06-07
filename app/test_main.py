import pytest
from unittest import mock

from app.main import can_access_google_page, has_internet_connection


@pytest.mark.parametrize("mock_internet, mock_valid, url, expected", [
    (True, True, "https://www.google.com", "Accessible"),
    (False, True, "https://www.safari.com", "Accessible"),
    (True, False, "https://www.google.com", "Not accessible"),
    (False, False, "https://www.mate.com", "Not accessible")
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_check_access_page(mock_internet_connection, mock_valid_google_url,
                           mock_internet, mock_valid, url, expected):

    mock_valid_google_url.return_value = mock_valid
    has_internet_connection.return_value = mock_internet

    assert can_access_google_page(url) == expected
