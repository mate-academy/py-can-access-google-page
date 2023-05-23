from unittest import mock
from app.main import can_access_google_page
from typing import Callable
import pytest


@pytest.fixture()
def mocked_url_validator() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_validator:
        yield mocked_validator


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_valid_url_and_connection(
        mocked_url_validator: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_internet_connection.return_value = True
    mocked_url_validator.return_value = True

    assert can_access_google_page("") == "Accessible"


def test_non_valid_url_no_connection(
        mocked_url_validator: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_internet_connection.return_value = False
    mocked_url_validator.return_value = False
    assert can_access_google_page("") == "Not accessible"


def test_non_valid_url_connection_exist(
        mocked_url_validator: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_internet_connection.return_value = True
    mocked_url_validator.return_value = False
    assert can_access_google_page("") == "Not accessible"


def test_valid_url_no_connection(
        mocked_url_validator: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_internet_connection.return_value = False
    mocked_url_validator.return_value = True
    assert can_access_google_page("") == "Not accessible"
