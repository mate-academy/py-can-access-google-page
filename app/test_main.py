import pytest

from unittest import mock

from app.main import can_access_google_page

from typing import Callable


@pytest.mark.parametrize(
    "is_connected,is_valid_url,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "You can access with connection and valid url",
        "You can't access without connection",
        "You can't access with invalid url",
        "You can't access without connection with invalid url"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_connection: Callable,
        mocked_valid_url: Callable,
        is_connected: bool,
        is_valid_url: bool,
        expected: str
) -> None:
    mocked_connection.return_value = is_connected
    mocked_valid_url.return_value = is_valid_url

    assert can_access_google_page("url") == expected
