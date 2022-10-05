import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked_function_url:
        yield mocked_function_url


@pytest.fixture()
def mocked_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_no_internet_connection(
        mocked_connection: Callable, mocked_url: Callable
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible"


def test_no_valid_url(
        mocked_connection: Callable, mocked_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"


def test_no_internet_connection_no_valid_url(
        mocked_connection: Callable, mocked_url: Callable
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"


def test_internet_connection_and_valid_url(
        mocked_connection: Callable, mocked_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible"
