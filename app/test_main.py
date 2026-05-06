import pytest
from unittest.mock import patch, MagicMock

from app import main


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    has_internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url

    result = main.can_access_google_page("https://google.com")

    assert result == expected
