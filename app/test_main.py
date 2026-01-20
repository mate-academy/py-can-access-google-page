from unittest.mock import MagicMock, patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("") == expected
