from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_has_internet:
        yield mock_has_internet


def test_function_valid_google_url_is_correct(mocked_has_internet_connection):
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("http://www.google.com/") == "Accessible"


def test_should_return_accessible(mocked_valid_url,
                                  mocked_has_internet_connection):
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("") == "Accessible"


def test_if_only_internet_connection_true(mocked_valid_url,
                                          mocked_has_internet_connection):
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("") == "Not accessible"


def test_if_only_valid_url_true(mocked_valid_url,
                                mocked_has_internet_connection):
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"
