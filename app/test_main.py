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
        "Accessible If we have valid google url and internet connection",
        "Not accessible If we have valid google url but don't have internet connection",
        "Not accessible If we don't have valid google url but have internet connection",
        "Not accessible If we don't have valid google url and internet connection",
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
    result = can_access_google_page("https://www.google.com")

    mock_valid_url.assert_called()

    if valid_google_url:
        mock_has_internet.assert_called_once()
    else:
        mock_has_internet.assert_not_called()

    assert result == expected
