import pytest

from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
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
    mocked_internet_connection: MagicMock,
    mocked_valid_url: MagicMock,
    valid_url: bool,
    internet_connection: bool,
    expected_result: str
) -> None:
    url = "https://www.example.com"
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    result = can_access_google_page(url)
    assert result == expected_result
