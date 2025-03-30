import pytest
from unittest import mock

from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mocked() -> tuple[Callable, Callable, str]:
    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        yield mock_valid_google_url, mock_has_internet_connection, "mock_url"


@pytest.mark.parametrize(
    "mocked_return_values, result",
    [
        ((True, True), "Accessible"),
        ((False, False), "Not accessible")
    ]
)
def test_return_expected_value(
        mocked: tuple,
        mocked_return_values: tuple,
        result: str
) -> None:
    mocked[0].return_value = mocked_return_values[0]
    mocked[1].return_value = mocked_return_values[1]

    assert can_access_google_page(mocked[2]) == result


def test_has_internet_connection_called(mocked: tuple) -> None:
    can_access_google_page(mocked[2])

    mocked[1].assert_called_once()


def test_valid_google_url_called(mocked: tuple) -> None:
    can_access_google_page(mocked[2])

    mocked[0].assert_called_once_with("mock_url")
