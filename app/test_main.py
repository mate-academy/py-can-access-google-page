from unittest import mock
import pytest
from app.main import can_access_google_page
from typing import Callable


@pytest.fixture()
def mocked_valid_google_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as \
            mock_has_internet_connection:
        yield mock_has_internet_connection


def test_when_valid_google_url_and_has_internet_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"


def test_when_valid_google_url_only(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"


def test_when_has_internet_connection_only(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


def test_when_no_internet_connection_and_invalid_google_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"
