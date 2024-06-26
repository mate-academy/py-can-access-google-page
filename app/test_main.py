import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid.url", False, True, "Not accessible"),
        ("https://invalid.url", False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet_connection: patch,
    mock_valid_url: patch,
    url: str,
    valid_url: bool,
    internet_connection: bool,
    expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection

    result = can_access_google_page(url)
    assert result == expected
