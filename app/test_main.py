import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mocked_valid_url: Callable,
        mocked_internet_connection: Callable,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection

    assert can_access_google_page("www.google.com/") == expected_result
