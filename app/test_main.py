import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch(
        "app.main.valid_google_url"
    ) as valid_url:
        yield valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as has_connection:
        yield has_connection


def test_wrong_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"


def test_invalid_google_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


def test_accessible(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("google.com") == "Accessible"
