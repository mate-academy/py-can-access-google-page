from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid URL and internet connection",
        "Invalid URL but internet connection",
        "Valid URL but no internet connection",
        "Invalid URL and no internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: mock.MagicMock,
    mock_valid_url: mock.MagicMock,
    valid_url: bool,
    internet_connection: bool,
    expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    result = can_access_google_page("https://anylink.com")

    mock_has_internet_connection.assert_called_once()

    if mock_has_internet_connection.assert_called_once():
        mock_valid_url.assert_called_once_with("https://anylink.com")

    assert result == expected
