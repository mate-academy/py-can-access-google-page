import pytest

from unittest import mock

from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_when_all_true(mocked_url: Callable,
                       mocked_connection: Callable
                       ) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible", (
        "The page is accessible with valid url and working internet"
    )


def test_internet_connection_is_false(mocked_url: Callable,
                                      mocked_connection: Callable
                                      ) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible", (
        "The page is not accessible with not working internet"
    )


def test_mocked_url_is_false(mocked_url: Callable,
                             mocked_connection: Callable
                             ) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible", (
        "The page is not accessible with not valid url"
    )


def test_both_functions_are_false(mocked_url: Callable,
                                  mocked_connection: Callable
                                  ) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible", (
        "The page is not accessible with both not working functions"
    )
