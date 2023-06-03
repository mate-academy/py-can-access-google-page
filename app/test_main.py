import pytest
from typing import Callable
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch(
        "app.main.valid_google_url"
    ) as valid_url:
        yield valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as has_connection:
        yield has_connection


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected_result",
    [
        pytest.param(True, True, "Accessible",
                     id="Should return Accessible"),
        pytest.param(False, True, "Not accessible",
                     id="Wrong connection"),
        pytest.param(True, False, "Not accessible",
                     id="Invalid google url"),
        pytest.param(False, False, "Not accessible",
                     id="Invalid google url and wrong_connection"),

    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        has_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = is_valid_url
    assert can_access_google_page("google.com") == expected_result
