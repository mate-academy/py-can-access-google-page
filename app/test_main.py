import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_has_internet, mock_valid_google, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: bool,
        mock_has_internet: MagicMock,
        mock_valid_google: bool,
        expected: str) -> None:
    mock_has_internet_connection.return_value = mock_has_internet
    mock_valid_google_url.return_value = mock_valid_google

    assert can_access_google_page("some url") == expected
