from unittest import mock
import pytest
from typing import Callable
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def has_internet_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_not_access_when_only_url_is_valid(
        mocked_valid_google_url: Callable,
        has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = True
    has_internet_connection.return_value = False
    assert can_access_google_page("test_url") == "Not accessible"


def test_not_access_when_only_connection_is_good(
        mocked_valid_google_url: Callable,
        has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = False
    has_internet_connection.return_value = True
    assert can_access_google_page("test_url") == "Not accessible"


def test_access_when_url_is_valid_and_connection_is_good(
        mocked_valid_google_url: Callable,
        has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = True
    has_internet_connection.return_value = True
    assert can_access_google_page("test_url") == "Accessible"


def test_not_access_when_url_invalid_and_connection_is_bad(
        mocked_valid_google_url: Callable,
        has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = False
    has_internet_connection.return_value = False
    assert can_access_google_page("test_url") == "Not accessible"
