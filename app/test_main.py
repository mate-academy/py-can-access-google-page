from typing import Any, Callable
from unittest import mock
from unittest.mock import MagicMock

import pytest

import app.main

url = "https://www.google.com/"


@pytest.fixture()
def mocked_has_internet_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection"
                    ) as mocked_has_internet_connection:
        yield mocked_has_internet_connection


@pytest.fixture()
def mocked_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url"
                    ) as mocked_valid_google_url:
        yield mocked_valid_google_url


def test_has_internet_connection_has_been_called(
        mocked_has_internet_connection: MagicMock) -> None:
    app.main.can_access_google_page(url)
    mocked_has_internet_connection.assert_called_once()


def test_valid_google_url_has_been_called_with_url(
        mocked_valid_google_url: MagicMock) -> None:
    app.main.can_access_google_page(url)
    mocked_valid_google_url.assert_called_once_with(url)


def test_accessible_when_both_validations_true(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    result = app.main.can_access_google_page(url)

    assert result == "Accessible"


def test_not_accessible_when_no_connection(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True

    result = app.main.can_access_google_page(url)

    assert result == "Not accessible"


def test_not_accessible_when_invalid_url(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    result = app.main.can_access_google_page(url)

    assert result == "Not accessible"
