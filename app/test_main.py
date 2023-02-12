import pytest

from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_incorrect_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("www.gog.co") == "Not accessible"


def test_no_internet_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_incorrect_url_and_no_internet_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_correct_url_and_has_internet_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("www.google.com") == "Accessible"
