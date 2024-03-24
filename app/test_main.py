from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url_value, connection_value, expected_value", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible")
], ids=[
    "Valid URL and connection",
    "Invalid URL but connection",
    "Valid URL but no connection",
    "Invalid URL and no connection"
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        valid_url_value: bool,
        connection_value: bool,
        expected_value: bool
) -> None:
    mock_valid_google_url.return_value = valid_url_value
    mock_has_internet_connection.return_value = connection_value
    assert can_access_google_page("https://www.google.com") == expected_value
