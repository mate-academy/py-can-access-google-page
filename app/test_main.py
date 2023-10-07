from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        valid_google_url: str,
        has_internet_connection: bool,
        expected: str
) -> None:

    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    result = can_access_google_page("https://google.com/")
    assert result == expected
