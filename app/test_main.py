from typing import Callable
from unittest import mock
from app.main import can_access_google_page

import pytest


@pytest.fixture
def test_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture
def test_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_incorrect_url(
        test_valid_google_url: Callable,
        test_has_internet_connection: Callable
) -> None:
    test_valid_google_url.return_value = False
    test_has_internet_connection.return_value = True

    assert can_access_google_page("www.gog.co") == "Not accessible"


def test_no_internet_connection(
        test_valid_google_url: Callable,
        test_has_internet_connection: Callable
) -> None:
    test_valid_google_url.return_value = True
    test_has_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_incorrect_url_and_no_internet_connection(
        test_valid_google_url: Callable,
        test_has_internet_connection: Callable
) -> None:
    test_valid_google_url.return_value = False
    test_has_internet_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_correct_url_and_has_internet_connection(
        test_valid_google_url: Callable,
        test_has_internet_connection: Callable
) -> None:
    test_valid_google_url.return_value = True
    test_has_internet_connection.return_value = True

    assert can_access_google_page("www.google.com") == "Accessible"
