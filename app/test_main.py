import pytest
from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection")\
            as mocked_connection:
        yield mocked_connection


def test_valid_url_and_has_connection(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True

    assert can_access_google_page("www.google.com") == "Accessible"


def test_valid_url_and_no_connection(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_wrong_url_and_has_connection(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_wrong_url_and_no_connection(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"
