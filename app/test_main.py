from unittest import mock

import pytest

from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url_validation() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked:
        yield mocked


@pytest.fixture()
def mocked_internet_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as mocked:
        yield mocked


def test_not_valid_google_url(mocked_internet_connection: Callable,
                              mocked_url_validation: Callable) -> None:
    mocked_url_validation.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible", (
        "Your google url is invalid")


def test_has_not_internet_connection(mocked_internet_connection: Callable,
                                     mocked_url_validation: Callable) -> None:
    mocked_internet_connection.return_value = False
    mocked_url_validation.return_value = True
    assert can_access_google_page("url") == "Not accessible", (
        "You have got unstable internet connection")


def test_bad_url_and_no_connection(mocked_internet_connection: Callable,
                                   mocked_url_validation: Callable) -> None:
    mocked_internet_connection.return_value = False
    mocked_url_validation.return_value = False
    assert can_access_google_page("url") == "Not accessible", (
        "You should to have stable internet and valid url")


def test_valid_url_and_connection(mocked_internet_connection: Callable,
                                  mocked_url_validation: Callable) -> None:
    mocked_url_validation.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("url") == "Accessible", (
        "You can access page with good internet connection and valid url")
