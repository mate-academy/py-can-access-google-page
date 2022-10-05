import pytest
# import requests
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_function_url:
        yield mocked_function_url


def test_should_check_url(mocked_url):
    mocked_url.return_value = True
    can_access_google_page("https://www.google.com/")
    mocked_url.assert_called_once_with("https://www.google.com/")


@pytest.fixture()
def mocked_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_function_connection:
        yield mocked_function_connection


def test_should_check_connection(mocked_connection):
    mocked_connection.return_value = True
    can_access_google_page("https://www.google.com/")
    mocked_connection.assert_called_once()


def test_no_internet_connection(mocked_connection, mocked_url):
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_no_valid_url(mocked_connection, mocked_url):
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"
