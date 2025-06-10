import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet_connected, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet: MagicMock,
        mock_valid_url: MagicMock,
        url_valid: bool,
        internet_connected: bool,
        expected: str) -> None:
    mock_valid_url.return_value = url_valid
    mock_internet.return_value = internet_connected

    test_url = "https://www.google.com"
    result = can_access_google_page(test_url)

    assert result == expected
