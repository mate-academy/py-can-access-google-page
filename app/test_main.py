from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page

GOOGLE_URL = "https://www.google.com"


@pytest.fixture()
def mocked_valid_google_url() -> Callable:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_test_valid:
        yield mock_test_valid


@pytest.fixture()
def mocked_has_internet_connection() -> Callable:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_test_connection:
        yield mock_test_connection


def test_should_call_both_func(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    can_access_google_page(GOOGLE_URL)
    try:
        mocked_valid_google_url.assert_called_once_with(GOOGLE_URL)
    except AssertionError as e:
        pytest.fail(f"You should call func with correct URL. Error: {e}")
    try:
        mocked_has_internet_connection.assert_called_once()
    except AssertionError as e:
        pytest.fail(f"You should call both check funcs. Error: {e}")


@pytest.mark.parametrize(
    "valid_url,connection,result", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ])
def test_should_return_correct_string(
        valid_url: bool,
        connection: bool,
        result: str,
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page(GOOGLE_URL) == result, (
        f"Expected {result} when valid url is {valid_url} "
        f"and internet connection is {connection}"
    )
