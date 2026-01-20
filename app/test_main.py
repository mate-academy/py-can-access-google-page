from typing import Callable
import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_valid_google_url_has_been_called(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    can_access_google_page("")
    mocked_valid_google_url.assert_called_once_with("")


def test_has_internet_connection_has_been_called(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    can_access_google_page("")
    mocked_has_internet_connection.assert_called()


@pytest.mark.parametrize(
    "current_url, internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        current_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = current_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("") == result
