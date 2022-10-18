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
        "Should be accessible when URL is valid and"
        "there is internet connection."
    )


def test_invalid_url_and_connection_exist(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Should return 'Not accessible' when URL isn't valid."
    )


def test_valid_url_and_connection_expire(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Should return 'Not accessible' when there is no internet connection."
    )


def test_invalid_url_and_connection_expire(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Should return 'Not accessible' when URL isn't valid."
        "and there is no internet connection."
    )
