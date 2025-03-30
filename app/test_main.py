from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def test_mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def test_mocked_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_all_is_good(test_mocked_url,
                     test_mocked_connection):
    test_mocked_url.return_value = True
    test_mocked_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible", \
        "You can get access only with internet connection and correct url"


def test_all_is_wrong(test_mocked_url,
                      test_mocked_connection):
    test_mocked_url.return_value = False
    test_mocked_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", \
        "You can`t get access without internet connection and with broke url"


def test_without_connection(test_mocked_url,
                            test_mocked_connection):
    test_mocked_url.return_value = True
    test_mocked_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", \
        "You can`t get access without internet connection"


def test_with_broke_url(test_mocked_url,
                        test_mocked_connection):
    test_mocked_url.return_value = False
    test_mocked_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible",\
        "You can`t get access with broke url"
