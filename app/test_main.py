from typing import Callable

import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google() -> None:
    with (mock.patch("app.main.valid_google_url")
          as mock_test_validation_google):
        yield mock_test_validation_google


def test_call_valid_google(mocked_valid_google: Callable) -> None:
    can_access_google_page("http://www.google.com")
    mocked_valid_google.return_value = True
    mocked_valid_google.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_call_has_internet_connection(
        mocked_internet_connection: Callable) -> None:
    can_access_google_page("http://www.google.com")
    mocked_internet_connection.return_value = True
    mocked_internet_connection.assert_called_once()


def test_google_com_should_return_accessible() -> None:
    assert can_access_google_page("http://www.google.com") == "Accessible"
