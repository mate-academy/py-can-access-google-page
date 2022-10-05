import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_if_all_work(
        mocked_valid_url,
        mocked_has_internet_connection
):
    mocked_has_internet_connection.return_value = True
    mocked_valid_url.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


def test_if_url_is_not_valid(
        mocked_valid_url,
        mocked_has_internet_connection
):
    mocked_has_internet_connection.return_value = True
    mocked_valid_url.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


def test_if_has_not_internet_connection(
        mocked_valid_url,
        mocked_has_internet_connection
):
    mocked_has_internet_connection.return_value = False
    mocked_valid_url.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"


def test_if_all_do_not_work(
        mocked_valid_url,
        mocked_has_internet_connection
):
    mocked_has_internet_connection.return_value = False
    mocked_valid_url.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"
