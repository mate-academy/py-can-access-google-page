import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize("url, mock_valid_url, mock_internet, expected", [
    ("https://google.com", True, True, "Accessible"),
    ("https://google.com", True, False, "Not accessible"),
    ("https://invalid-url.com", False, True, "Not accessible"),
    ("https://invalid-url.com", False, False, "Not accessible"),
]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet_connection: mock.Mock,
        mock_valid_google_url: mock.Mock,
        url: str,
        mock_valid_url: bool,
        mock_internet: bool,
        expected: str) -> None:
    mock_valid_google_url.return_value = mock_valid_url
    mock_internet_connection.return_value = mock_internet

    result = can_access_google_page(url)

    assert result == expected
