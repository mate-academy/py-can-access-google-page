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


@pytest.mark.parametrize(
    "internet_connection, url_validator, result",
    [
        pytest.param(True, True, "Accessible",
                     id="test valid url and connection"),
        pytest.param(False, False, "Not accessible",
                     id="test non valid url no connection"),
        pytest.param(True, False, "Not accessible",
                     id="test non valid url connection exist"),
        pytest.param(False, True, "Not accessible",
                     id="test valid url no connection")
    ]
)
def test_return_correct_value(mocked_url_validator: Callable,
                              mocked_internet_connection: Callable,
                              url_validator: bool,
                              internet_connection: bool,
                              result: str) -> None:
    mocked_internet_connection.return_value = internet_connection
    mocked_url_validator.return_value = url_validator
    assert can_access_google_page("") == result
