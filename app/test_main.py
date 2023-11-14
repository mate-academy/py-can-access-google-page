import pytest
from unittest.mock import patch

from app.main import (can_access_google_page)


@pytest.mark.parametrize(
    "url, has_internet, is_valid, expected_result",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("", False, True, "Not accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("", False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    url: str,
    has_internet: bool,
    is_valid: bool,
    expected_result: str
) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet_connection.return_value = has_internet

    result = can_access_google_page(url)

    assert result == expected_result
