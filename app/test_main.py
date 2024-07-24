from unittest import mock
from typing import Callable
import pytest
from app.main import can_access_google_page


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
    can_access_google_page("https://www.google.com")
    mocked_valid_google_url.assert_called_once_with("https://www.google.com")
    mocked_has_internet_connection.assert_called_once()


def test_should_return_correct_string(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
