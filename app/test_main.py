from collections.abc import Generator

from unittest.mock import Mock

from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_google_url() -> Generator:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture
def mocked_has_internet_connection() -> Generator:
    with (
        mock.patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        yield mock_has_internet_connection


def test_func_usage_valid_google(mocked_valid_google_url: Mock) -> None:
    can_access_google_page("https://www.google.com")
    mocked_valid_google_url.assert_called_once()


def test_func_usage_has_internet_connection(
        mocked_has_internet_connection: Mock
) -> None:
    can_access_google_page("https://www.google.com")
    mocked_has_internet_connection.assert_called_once()


def test_main_func_access(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_main_func_not_access_both_false(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

def test_main_func_not_access_first_false(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

def test_main_func_not_access_second_false(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
