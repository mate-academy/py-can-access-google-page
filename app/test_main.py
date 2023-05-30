# from app.main import can_access_google_page
# import pytest
# from unittest import mock
# from typing import Callable
# from requests.exceptions import (MissingSchema, InvalidSchema,
#                                  ConnectionError)


def test_url_type_valid_missingschema() -> None:
    with pytest.raises(MissingSchema):
        can_access_google_page(1)


def test_url_type_valid_invalidschema() -> None:
    with pytest.raises(InvalidSchema):
        can_access_google_page("htt://mate.academy/")


def test_url_type_valid_connectionerror() -> None:
    with pytest.raises(ConnectionError):
        can_access_google_page("https://nonexistentwebsite.com")


@pytest.fixture()
def mocked_url_valid_check() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_internet_connection_check() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_true_conditions(mocked_url_valid_check: Callable,
                         mocked_internet_connection_check: Callable
                         ) -> None:
    mocked_url_valid_check.return_value = True
    mocked_internet_connection_check.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Accessible"


def test_false_conditions(mocked_url_valid_check: Callable,
                          mocked_internet_connection_check: Callable
                          ) -> None:
    mocked_url_valid_check.return_value = False
    mocked_internet_connection_check.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_invalid_url(mocked_url_valid_check: Callable,
                     mocked_internet_connection_check: Callable
                     ) -> None:
    mocked_url_valid_check.return_value = False
    mocked_internet_connection_check.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_no_internet_connection(mocked_url_valid_check: Callable,
                                mocked_internet_connection_check: Callable
                                ) -> None:
    mocked_url_valid_check.return_value = True
    mocked_internet_connection_check.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"
