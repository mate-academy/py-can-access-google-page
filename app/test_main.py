from unittest.mock import MagicMock, patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expected",
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
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
    valid_url: bool,
    connection: bool,
    expected: str,
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = connection

    result = can_access_google_page("https://www.google.com")

    assert result == expected
