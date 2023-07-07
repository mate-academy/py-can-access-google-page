from typing import Callable
from unittest import mock

from .main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_has_called(mocked_valid_url: Callable) -> None:

    can_access_google_page("https://www.google.com/")

    mocked_valid_url.assert_called_once


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection(mocked_valid_inet: Callable) -> None:

    can_access_google_page("https://www.google.com/")

    mocked_valid_inet.assert_called_once


def test_can_access_page() -> None:
    assert can_access_google_page("https://www.google.com/")
