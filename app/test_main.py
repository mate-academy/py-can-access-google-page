import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "connection_status, url_validation, expected",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "No connection",
        "Invalid `URL`",
        "Connection OK, Valid `URL`",
        "No connection, Invalid `URL`"
    ]
)
def test_can_access_to_google_page(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock,
        connection_status: bool,
        url_validation: bool,
        expected: str) -> None:
    mocked_has_internet_connection.return_value = connection_status
    mocked_valid_google_url.return_value = url_validation
    assert can_access_google_page("https://www.google.com") == expected
