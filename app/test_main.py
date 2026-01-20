import pytest
from unittest.mock import patch
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, valid_internet, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet: Callable,
                                mock_valid_url: Callable,
                                url: str,
                                valid_url: bool,
                                valid_internet: bool,
                                expected: str
                                ) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet.return_value = valid_internet
    result = can_access_google_page(url)
    assert result == expected
