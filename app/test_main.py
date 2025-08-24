# app/test_main.py

import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url, is_valid, has_internet, expected",
    [
        (
            "https://www.google.com",
            True,
            True,
            "Accessible"
        ),
        (
            "https://www.google.com",
            True,
            False,
            "Not accessible"
        ),
        (
            "https://www.fake-google.com",
            False,
            True,
            "Not accessible"
        ),
        (
            "https://www.fake-google.com",
            False,
            False,
            "Not accessible"
        ),
    ]
)
def test_can_access_google_page(
    mock_internet: object,
    mock_valid_url: object,
    url: str,
    is_valid: bool,
    has_internet: bool,
    expected: str
) -> None:
    mock_valid_url.return_value = is_valid
    mock_internet.return_value = has_internet

    result = can_access_google_page(url)
    assert result == expected
