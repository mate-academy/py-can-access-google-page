from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_google_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture
def mocked_has_internet_connection() -> Callable:
    with (
        mock.patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        yield mock_has_internet_connection


def test_valid_url_and_connection_exists(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert (
        can_access_google_page("url") == "Accessible"
    ), "Should be 'Accessible' with valid url and existing connection"


def test_non_valid_url_and_connection_exists(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert (
        can_access_google_page("url") == "Not accessible"
    ), "Should be 'Not accessible' with not valid url and existing connection"


def test_valid_url_and_no_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page("url") == "Not accessible"
    ), "Should be 'Not accessible' with valid url and non existing connection"


def test_non_valid_url_and_no_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page("url") == "Not accessible"
    ), "Should be 'Not accessible' with non valid url and no connection"
