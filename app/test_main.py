from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, can_access_google",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_function(
        mocked_connection: bool,
        mocked_url: bool,
        valid_google_url: bool,
        has_internet_connection: bool,
        can_access_google: object,
) -> None:
    mocked_url.return_value = valid_google_url
    mocked_connection.return_value = has_internet_connection
    assert can_access_google_page("https://google.com") == can_access_google
