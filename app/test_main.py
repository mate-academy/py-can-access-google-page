import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "has_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mock_has_internet: MagicMock,
        mock_valid_url: MagicMock,
        has_connection: bool,
        valid_url: bool,
        expected: str,
) -> None:
    mock_has_internet.return_value = has_connection
    mock_valid_url.return_value = valid_url

    result = can_access_google_page("https://www.google.com")
    assert result == expected
