from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        internet_connection: bool,
        valid_url: bool,
        expected: str) -> None:
    mock_valid_google_url.return_value = internet_connection
    mock_has_internet_connection.return_value = valid_url
    result = can_access_google_page("https://www.google.com")
    assert result == expected
