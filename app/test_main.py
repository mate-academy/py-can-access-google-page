import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_valid_url_and_connection_exist(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True

    assert can_access_google_page("www.google.com/") == "Accessible", (
        "Accessible: url is valid to access the Google home page and"
        "it has internet connection"
    )


def test_invalid_url_and_connection_exist(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "There is no internet connection."
        "Internet connection exists only between 6:00:00 and 22:59:59"
    )


def test_valid_url_and_connection_expire(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Current url isn't valid to access the Google home page."
    )


def test_invalid_url_and_connection_expire(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Current url isn't valid to access the Google home page."
        "There is no internet connection"
    )
