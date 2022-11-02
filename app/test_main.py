import pytest
from unittest import mock
from typing import Any

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> Any:
    with (mock.patch("app.main.valid_google_url")
          as mocked_test_valid):
        yield mocked_test_valid


@pytest.fixture()
def mocked_has_connection() -> Any:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_internet):
        yield mocked_internet


def test_called_valid_google_url_with_right_parameters(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    can_access_google_page("google.com.ua")
    mocked_valid_google_url.assert_called_once_with("google.com.ua")


def test_called_has_internet_connection(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    can_access_google_page("google.com.ua")
    mocked_has_connection.assert_called_once


def test_should_return_not_accessible_when_url_not_valid(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_connection.return_value = True
    assert (can_access_google_page("google.com.ua")
            == "Not accessible")


def test_should_return_not_accessible_when_connection_not_exist(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    mocked_has_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert (can_access_google_page("google.com.ua")
            == "Not accessible")


def test_should_return_not_accessible_when_url_not_valid_and(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    mocked_has_connection.return_value = False
    mocked_has_connection.return_value = False
    assert (can_access_google_page("google.com.ua")
            == "Not accessible")


def test_should_return_accessible_when_url_valid_and_connection_exist(
        mocked_valid_google_url: Any, mocked_has_connection: Any
) -> None:
    mocked_has_connection.return_value = True
    mocked_has_connection.return_value = True
    assert (can_access_google_page("google.com.ua")
            == "Accessible")
