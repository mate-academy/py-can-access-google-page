import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        yield mocked_validation


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_for_correct_values(mocked_valid_google_url,
                            mocked_has_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://mate.academy/learn?course=python") \
           == "Accessible", "Function must return 'Accessible' " \
                            "if url is valid and current time is correct!"


def test_for_not_valid_url(mocked_valid_google_url,
                           mocked_has_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://twitter.com/[username].") \
           == "Not accessible", "Function must return 'Not accessible' " \
                                "if url is not valid!"


def test_for_incorrect_time(mocked_valid_google_url,
                            mocked_has_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") \
           == "Not accessible", "Function must return 'Not accessible' " \
                                "if current time is not correct!"


def test_for_not_correct_values(mocked_valid_google_url,
                                mocked_has_internet_connection):
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://www.example.com/space%20here.html") \
           == "Not accessible", "Function must return 'Not accessible' if " \
                                "url is not valid and current time is " \
                                "incorrect!"
