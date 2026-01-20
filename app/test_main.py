import pytest

from app.main import can_access_google_page
from unittest import mock

url = "www.google.com"


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url",
                    return_value=True) as \
            mocked_valid_google_url:
        yield mocked_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection",
                    return_value=True) as \
            mocked_has_internet_connection:
        yield mocked_has_internet_connection


def test_should_call_func_valid(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    can_access_google_page(url)
    mocked_valid_google_url.assert_called_once_with(url)


def test_should_call_func_internet_connection(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    can_access_google_page(url)
    mocked_has_internet_connection.assert_called_once()


def test_return_access_if_both_methods_is_true(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    assert can_access_google_page(url) == "Accessible"


def test_return_not_accessible_if_connection_fail(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"


def test_return_not_accessible_if_validation_is_fail(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"


def test_return_not_accessible_if_validation_and_accessible_is_fail(
        mocked_valid_google_url,
        mocked_has_internet_connection
):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"
