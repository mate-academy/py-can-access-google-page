import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture()
def mocked_has_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_has_connection:
        yield mock_has_connection


def test_valid_google_url_has_been_called(
        mocked_valid_google_url: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    can_access_google_page("")
    mocked_valid_google_url.assert_called_once_with("")


def test_has_internet_connection_has_been_called(
        mocked_valid_google_url: Callable,
        mocked_has_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_connection.return_value = True
    can_access_google_page("")
    mocked_has_connection.assert_called()


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page_result(
        mocked_valid_google_url: Callable,
        mocked_has_connection: Callable,
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_connection.return_value = has_internet_connection
    assert can_access_google_page("") == result
