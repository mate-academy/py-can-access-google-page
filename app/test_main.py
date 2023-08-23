from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_has_internet_connection:
        yield mock_has_internet_connection


def test_functions_was_called(mocked_has_internet_connection, mocked_valid_google_url):
    can_access_google_page("https://www.google.com/")
    mocked_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()


def test_not_accessible_url(mocked_has_internet_connection, mocked_valid_google_url):
    mocked_valid_google_url.return_value = False

    result = can_access_google_page("http://httpstat.us/400")

    assert result == "Not accessible"


def test_not_accessible_internet_connection(mocked_has_internet_connection, mocked_valid_google_url):
    mocked_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com/")

    assert result == "Not accessible"


def test_accessible_page(mocked_has_internet_connection, mocked_valid_google_url):
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com/")

    assert result == "Accessible"

