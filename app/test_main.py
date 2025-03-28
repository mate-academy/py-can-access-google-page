from app.main import can_access_google_page
from unittest import mock
from typing import Callable

import pytest


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_test_url:
        yield mock_test_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mock_test_connection:
        yield mock_test_connection


def test_not_valid_googl_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_internet_connection_does_not_have(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_not_valid_googl_url_and_internet_connection_does_not_have(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_valid_googl_url_and_has_internet_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("www.googl.com") == "Accessible"
