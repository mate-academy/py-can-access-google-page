from app.main import can_access_google_page
from typing import Callable
from unittest import mock

import pytest


@pytest.fixture()
def test_mock_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_test_url:
        yield mock_test_url


@pytest.fixture()
def test_mock_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_test_connection):
        yield mock_test_connection


def test_not_valid_googl_url(
        test_mock_google_url: Callable,
        test_mock_internet_connection: Callable
) -> None:
    test_mock_google_url.return_value = False
    test_mock_internet_connection.return_value = True
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_doesnt_have_internet_connection(
        test_mock_google_url: Callable,
        test_mock_internet_connection: Callable
) -> None:
    test_mock_google_url.return_value = True
    test_mock_internet_connection.return_value = False
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_not_valid_googl_url_and_doesnt_have_internet_connection(
        test_mock_google_url: Callable,
        test_mock_internet_connection: Callable
) -> None:
    test_mock_google_url.return_value = False
    test_mock_internet_connection.return_value = False
    assert can_access_google_page("www.googl.com") == "Not accessible"


def test_valid_googl_url_and_has_internet_connection(
        test_mock_google_url: Callable,
        test_mock_internet_connection: Callable
) -> None:
    test_mock_google_url.return_value = True
    test_mock_internet_connection.return_value = True
    assert can_access_google_page("www.googl.com") == "Accessible"
