# write your code here
from unittest import mock
from unittest.mock import MagicMock, AsyncMock

import pytest

from app.main import can_access_google_page
from typing import Any, Generator


@pytest.fixture
def mocked_url() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch("app.main.valid_google_url") as mocked_test_url:
        yield mocked_test_url


@pytest.fixture
def mocked_connection() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch("app.main.has_internet_connection") as mocked_t_connection:
        yield mocked_t_connection


def test_url_was_called(
        mocked_url: MagicMock
) -> None:
    can_access_google_page("test")
    mocked_url.assert_called_with("test")


def test_connection_was_called(
        mocked_connection: MagicMock,
        mocked_url: MagicMock
) -> None:
    can_access_google_page("test")
    mocked_connection.assert_called()


def test_func_return_true_if_both_are_true(
        mocked_connection: MagicMock,
        mocked_url: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("test") == "Accessible"


def test_func_return_false_if_no_connection(
        mocked_connection: MagicMock,
        mocked_url: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("test") == "Not accessible"


def test_func_return_false_if_invalid_url(
        mocked_connection: MagicMock,
        mocked_url: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("test") == "Not accessible"


def test_func_return_false_if_invalid_url_and_no_connection(
        mocked_connection: MagicMock,
        mocked_url: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("test") == "Not accessible"
