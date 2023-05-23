import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("url, valid_url, internet_connection, expected_result", [
    ("https://www.google.com", True, True, "Accessible"),
    ("https://www.google.com", True, False, "Not accessible"),
    ("https://www.invalidurl.com", False, True, "Not accessible"),
])
def test_can_access_google_page(url, valid_url, internet_connection, expected_result):
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url, \
            mock.patch("app.main.has_internet_connection") as mock_has_internet_connection:
        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = internet_connection

        result = can_access_google_page(url)
        assert result == expected_result
