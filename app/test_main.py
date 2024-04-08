from unittest.mock import MagicMock, patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Access granted with internet and valid URL",
        "Access denied without valid URL",
        "Access denied without internet connection",
        "Access denied without internet connection and valid URL",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url

    assert can_access_google_page("https://www.google.com") == expected_result

    mock_has_internet_connection.assert_called_once()
    if has_internet_connection:
        mock_valid_google_url.assert_called_once()
