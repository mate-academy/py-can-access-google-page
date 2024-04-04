import pytest
from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_output",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_connection_or_valid_url_is_true(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_output: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    assert can_access_google_page("https://www.google.com/") == expected_output
