import pytest
from unittest.mock import patch
from typing import Callable
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected_result", [
    ("http://www.google.com", True, "Accessible"),
    ("", True, "Not accessible"),
    ("http://www.google.com", False, "Not accessible"),
    ("", False, "Not accessible"),
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: Callable,
        mock_valid_url: Callable,
        valid_url: str,
        has_connection: bool,
        expected_result: str) -> None:
    mock_has_internet.return_value = has_connection
    mock_valid_url.return_value = bool(valid_url)

    assert can_access_google_page(valid_url) == expected_result
