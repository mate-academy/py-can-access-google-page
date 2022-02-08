import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_internet_connection:
        yield mocked_internet_connection


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        yield mocked_valid_google_url


def test_invalid_url(mocked_valid_google_url, mocked_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = True

    assert can_access_google_page("https://qwerty2323.com") == "Not accessible"


def test_no_connection(mocked_valid_google_url, mocked_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_no_connection_with_invalid_url(mocked_valid_google_url, mocked_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_internet_connection.return_value = False

    assert can_access_google_page("https://qwerty2323.com") == "Not accessible"


def test_connection_with_valid_url(mocked_valid_google_url, mocked_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_internet_connection.return_value = True

    assert can_access_google_page("http://google.com") == "Accessible"
