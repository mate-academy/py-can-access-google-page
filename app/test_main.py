import pytest

from app.main import can_access_google_page

from unittest import mock

from typing import Callable


@pytest.fixture()
def mocked_valid_google_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mock_connection:
        yield mock_connection


@pytest.fixture()
def mocked_has_internet_connection() -> mock:
    with mock.patch("app.main.has_internet_connection") as mock_time:
        yield mock_time


def test_access_google_page_true(
    mocked_valid_google_url: Callable, mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible"


def test_access_google_page_connection_fail(
    mocked_valid_google_url: Callable, mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page("www.google.com") == "Not accessible"
    ), "Bad connection"


def test_access_google_page_url_fail(
    mocked_valid_google_url: Callable, mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert (
        can_access_google_page("www.google.com") == "Not accessible"
    ), "Wrong url"


def test_access_google_page_wrong_url(
    mocked_valid_google_url: Callable, mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page("www.rambler.com") == "Not accessible"
    ), "Check your connection and url"
