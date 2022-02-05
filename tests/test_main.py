from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_int():
    with mock.patch("app.main.has_internet_connection") as mock_int_con:
        yield mock_int_con


@pytest.fixture()
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


def test_should_check_internet_true_and_url_true(mocked_int, mocked_url):
    mocked_int.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("") == "Accessible"


def test_should_check_internet_true_and_url_false(mocked_int, mocked_url):
    mocked_int.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page([]) == "Not accessible"


def test_should_check_internet_false_and_url_true(mocked_int, mocked_url):
    mocked_int.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page(()) == "Not accessible"


def test_should_check_internet_false_and_url_false(mocked_int, mocked_url):
    mocked_int.return_value = False
    mocked_url.return_value = False
    assert can_access_google_page({}) == "Not accessible"
