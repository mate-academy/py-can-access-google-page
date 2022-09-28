import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_has_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_when_all_works(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible",\
        "Page is accessible only with internet connection and valid url."


def test_no_valid_url(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible",\
        "Page is not accessible when url is not valid."


def test_no_internet_connection(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible",\
        "Page is not accessible if internet connection is down."


def test_when_all_is_broken(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible",\
        "Page is not accessible when all goes wrong."
