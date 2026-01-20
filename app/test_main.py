import pytest
from unittest import mock
from typing import Any, Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocking_valid_google_url() -> Any:
    with mock.patch("app.main.valid_google_url") as func:
        func.return_value = True
        yield func


@pytest.fixture()
def mocked_has_internet_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as func:
        func.return_value = True
        yield func


def test_main_func_using_required_funcs(
    mocking_valid_google_url: Callable,
    mocked_has_internet_connection: Callable
) -> None:
    can_access_google_page("")
    mocking_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()
