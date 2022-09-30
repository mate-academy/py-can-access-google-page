from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_has_internet:
        yield mock_has_internet


def test_all_works(mocked_valid_url, mocked_has_internet_connection):
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible", \
        "Can get access only with internet connection and valid url"


def test_no_connection(mocked_valid_url, mocked_has_internet_connection):
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", \
        "Cannot get access without internet connection"


def test_not_response(mocked_valid_url, mocked_has_internet_connection):
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible", \
        "Cannot get access with invalid url"


def test_all_false(mocked_valid_url, mocked_has_internet_connection):
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", \
        "Cannot get access without internet connection and with invalid url"
