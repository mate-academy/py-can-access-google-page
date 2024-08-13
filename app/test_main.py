# write your code here
from unittest.mock import patch

import pytest

from app.main import can_access_google_page


url = "https://www.google.com"


@pytest.mark.parametrize(
    "test_url,valid_google_url,has_internet_connection,expected",
    [
        (url, True, True, "Accessible"),
        (url, True, False, "Not accessible"),
        (url, False, True, "Not accessible"),
        (url, False, False, "Not accessible"),
    ],
    ids=[
        "If we have valid google url and internet connection",
        "If we have valid google url but don't have internet connection",
        "If we don't have valid google url but have internet connection",
        "If we don't have valid google url and internet connection",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_correct(
        mock_valid_url: bool,
        mock_has_internet: bool,
        test_url: str,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_google_url
    mock_has_internet.return_value = has_internet_connection

    result = can_access_google_page(test_url)
    assert result == expected
