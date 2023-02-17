import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,valid_url,connection_exists,message",
    [
        ("http://www.google.com/", True, True, "Accessible"),
        ("http://www.google.com/", True, False, "Not accessible"),
        ("http://www.google.com/", False, True, "Not accessible"),
        ("http://www.google.com/", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        valid_google_url: Callable,
        has_internet_connection: Callable,
        url: str,
        valid_url: bool,
        connection_exists: bool,
        message: str
) -> None:
    valid_google_url.return_value = valid_url
    has_internet_connection.return_value = connection_exists
    assert can_access_google_page(url) == message
