from unittest import mock
import pytest
from app.main import can_access_google_page as access


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url")\
            as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection")\
            as mocked_internet_connection:
        yield mocked_internet_connection


def test_valid_google_url_was_called(mocked_valid_url,
                                     mocked_internet_connection):
    access(" ")
    mocked_valid_url.assert_called_once()


def test_has_internet_connection_was_called(mocked_valid_url,
                                            mocked_internet_connection):
    access(" ")
    mocked_internet_connection.assert_called_once()


def test_not_accessible_when_url_false(mocked_valid_url,
                                       mocked_internet_connection):
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert access("") == "Not accessible"


def test_not_accessible_when_no_connection(mocked_valid_url,
                                           mocked_internet_connection):
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert access("") == "Not accessible"


def test_not_accessible_no_connection_false_url(mocked_valid_url,
                                                mocked_internet_connection):
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert access("") == "Not accessible"


def test_should_return_accessible(mocked_valid_url,
                                  mocked_internet_connection):
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True
    assert access("") == "Accessible"
