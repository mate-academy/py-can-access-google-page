from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
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
def test_can_access_google_page(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_google_url
    mock_has_internet.return_value = has_internet_connection

    assert can_access_google_page("https://www.google.com") == expected
