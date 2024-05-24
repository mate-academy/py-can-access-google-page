from unittest import mock
from typing import Any, Callable

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url_check() -> Any:
    with (mock.patch("app.main.valid_google_url")
          as mock_url_check):
        yield mock_url_check


@pytest.fixture()
def mocked_internet_connection_check() -> Any:
    with (mock.patch("app.main.has_internet_connection")
          as mock_connection_check):
        yield mock_connection_check


def test_valid_url_call(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    url = "https://example.com/"
    can_access_google_page(url)
    mocked_valid_url_check.assert_called_once_with(url)


def test_internet_connection_call(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    url = "https://example.com/"
    can_access_google_page(url)
    mocked_internet_connection_check.assert_called_once()


def test_response_no_internet(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    mocked_internet_connection_check.return_value = False
    url = "https://example.com/"
    assert can_access_google_page(url) == "Not accessible"


def test_response_invalid_url(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    mocked_valid_url_check.return_value = False
    assert can_access_google_page("example") == "Not accessible"


def test_response_invalid_url_and_no_internet(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    mocked_internet_connection_check.return_value = False
    mocked_valid_url_check.return_value = False
    assert can_access_google_page("example") == "Not accessible"


def test_response_valid_url_and_internet_connection(
        mocked_valid_url_check: Callable,
        mocked_internet_connection_check: Callable
) -> None:
    mocked_internet_connection_check.return_value = True
    mocked_valid_url_check.return_value = True
    url = "https://example.com/"
    assert can_access_google_page(url) == "Accessible"
