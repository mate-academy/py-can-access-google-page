import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_url, mock_connect, url, connection, expected):
    url_address = "www.google.com"
    mock_connect.return_value = connection
    mock_valid_url.return_value = url
    assert can_access_google_page(url_address) == expected
