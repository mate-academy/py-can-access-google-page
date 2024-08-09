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


def test_should_return_correct_string(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    assert can_access_google_page(GOOGLE_URL) == "Accessible", (
        "Should return correct string when both func are True"
    )
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(GOOGLE_URL) == "Not accessible", (
        "Expected 'Not accessible' when one func is False"
    )
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(GOOGLE_URL) == "Not accessible", (
        "Expected 'Not accessible' when one func is False"
    )
