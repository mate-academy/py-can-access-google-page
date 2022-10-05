from unittest import mock
from typing import Callable

from app.main import can_access_google_page

URL = "https://www.google.com/"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_both_not_valid(
        mocked_google_url: Callable,
        mocked_internet: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet.return_value = False

    assert can_access_google_page(URL) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_bad_internet(
        mocked_google_url: Callable,
        mocked_internet: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet.return_value = False

    assert can_access_google_page(URL) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_bad_url(
        mocked_google_url: Callable,
        mocked_internet: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet.return_value = True

    assert can_access_google_page(URL) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_both_valid(
        mocked_google_url: Callable,
        mocked_internet: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet.return_value = True

    assert can_access_google_page(URL) == "Accessible"
