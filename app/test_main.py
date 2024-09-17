from typing import Callable

from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mocked_has_connection:
        yield mocked_has_connection


def test_if_google_url_is_not_valid(
        mocked_valid_url: Callable,
        mocked_has_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("some url") == "Not accessible"


def test_if_has_no_internet_connection(
        mocked_valid_url: Callable,
        mocked_has_connection: Callable
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("some url") == "Not accessible"


def test_if_url_is_not_valid_and_no_internet_connection(
        mocked_valid_url: Callable,
        mocked_has_connection: Callable
) -> None:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = False
    assert can_access_google_page("some url") == "Not accessible"


def test_valid_url_and_connection_exists(
        mocked_valid_url: Callable,
        mocked_has_connection: Callable
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("some url") == "Accessible"
