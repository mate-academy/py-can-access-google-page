import pytest

from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        internet_connection: bool,
        valid_url: bool,
        expected: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == expected
