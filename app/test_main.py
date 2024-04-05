from unittest.mock import MagicMock, patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_output",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid URL and internet connection available",
        "Valid URL but no internet connection",
        "Internet connection available but invalid URL",
        "No internet connection and invalid URL"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_with_different_connection_and_url_states(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_output: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    assert can_access_google_page("https://www.google.com/") == expected_output
    mock_valid_google_url.assert_called_once()
    if valid_url:
        mock_has_internet_connection.assert_called_once()
    else:
        mock_has_internet_connection.assert_not_called()
