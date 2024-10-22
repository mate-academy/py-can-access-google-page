import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid_url, is_connected, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.invalid_url.com", False, True, "Not accessible"),
        ("https://www.invalid_url.com", False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet_connection: patch,
        mock_valid_url: patch,
        url: str,
        is_valid_url: bool,
        is_connected: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_internet_connection.return_value = is_connected
    result = can_access_google_page(url)
    assert result == expected, f"Expected {expected}, but got {result}"
