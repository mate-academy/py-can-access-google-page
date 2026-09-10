from typing import Any
from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,url_valid,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: Any,
    mock_internet: Any,
    internet: bool,
    url_valid: bool,
    expected: str,
) -> None:
    mock_internet.return_value = internet
    mock_valid_url.return_value = url_valid
    result = can_access_google_page("https://google.com")
    assert result == expected