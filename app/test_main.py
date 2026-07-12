from typing import Any
from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, has_internet, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_url_and_internet_combinations(
    mock_url: Any,
    mock_internet: Any,
    url_valid: bool,
    has_internet: bool,
    expected: str,
) -> None:
    mock_url.return_value = url_valid
    mock_internet.return_value = has_internet
    assert can_access_google_page("https://www.google.com") == expected
