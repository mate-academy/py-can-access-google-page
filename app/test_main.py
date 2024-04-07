from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_parameter,has_internet_connection_parameter,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Valid URL and internet connection",
        "Valid URL but no internet connection",
        "Invalid URL but internet connection available",
        "Invalid URL and no internet connection"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        valid_google_url: mock.MagicMock,
        has_internet_connection: mock.MagicMock,
        valid_google_url_parameter: bool,
        has_internet_connection_parameter: bool,
        expected: str
) -> None:
    valid_google_url.return_value = valid_google_url_parameter
    has_internet_connection.return_value = has_internet_connection_parameter
    assert can_access_google_page("") == expected
    valid_google_url.assert_called_once()
    if not valid_google_url:
        has_internet_connection.assert_called_once()
