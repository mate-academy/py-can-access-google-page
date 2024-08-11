from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_connection_true(
    mocked_valid_google_url: any,
    mocked_has_internet_connection: any,
    url: bool,
    connection: bool,
    expected: str
) -> None:
    url1 = "https://www.google.com"

    mocked_has_internet_connection.return_value = url
    mocked_valid_google_url.return_value = connection

    assert can_access_google_page(url1) == expected