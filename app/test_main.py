import pytest
from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected",
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
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet_connection.return_value = internet
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page("https://www.google.com")

    assert result == expected
