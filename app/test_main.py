import pytest
from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


@pytest.mark.parametrize("valid_url, internet_connection, expected_result", [
    ("https://www.google.com", True, "Accessible"),
    ("https://invalid-url.com", True, "Not accessible"),
    ("https://www.google.com", False, "Not accessible")
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: Callable,
    mock_valid_google_url: Callable,
    valid_url: str,
    internet_connection: bool,
    expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    if valid_url == "https://invalid-url.com":
        mock_valid_google_url.return_value = False
    else:
        mock_valid_google_url.return_value = True
    result = can_access_google_page(valid_url)
    assert result == expected_result
