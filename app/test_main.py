from unittest import mock
from unittest.mock import MagicMock
from typing import Generator

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> Generator[MagicMock, None, None]:
    with mock.patch("app.main.valid_google_url") as mocked_valid:
        yield mocked_valid


@pytest.fixture()
def mocked_has_internet_connection() -> Generator[MagicMock, None, None]:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_internet_connection):
        yield mocked_internet_connection


def test_should_call_function_valid_google_url_with_url(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock
) -> None:
    mocked_has_internet_connection.return_value = True

    can_access_google_page("https://www.google.com/")
    mocked_valid_google_url.assert_called_once_with("https://www.google.com/")


def test_should_call_function_has_internet_connection(
        mocked_has_internet_connection: MagicMock
) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_has_internet_connection.assert_called_once()


def test_should_return_accessible_if_all_requirements_are_done(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com/")
    assert result == "Accessible"


def test_should_return_not_accessible_if_internet_connection_lost(
        mocked_has_internet_connection: MagicMock
) -> None:

    mocked_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com/")
    assert result == "Not accessible"


def test_should_return_not_accessible_if_page_is_not_valid(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock
) -> None:

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    result = can_access_google_page("https://www.google.com/")
    assert result == "Not accessible"
