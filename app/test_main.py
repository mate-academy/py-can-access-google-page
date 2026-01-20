import pytest
from app.main import can_access_google_page
from unittest import mock
from typing import Callable


@pytest.fixture()
def mocked_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mocked_internet_connection:
        yield mocked_internet_connection


def test_when_internet_is_true_and_url_is_true(
        mocked_url: Callable,
        mocked_internet_connection: Callable,
) -> None:
    mocked_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("") == "Accessible"


def test_when_internet_is_false_and_url_is_false(
        mocked_url: Callable,
        mocked_internet_connection: Callable,
) -> None:
    mocked_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"


def test_when_internet_is_true_and_url_is_false(
        mocked_url: Callable,
        mocked_internet_connection: Callable,
) -> None:
    mocked_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"


def test_when_internet_is_false_and_url_is_true(
        mocked_url: Callable,
        mocked_internet_connection: Callable,
) -> None:
    mocked_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("") == "Not accessible"
