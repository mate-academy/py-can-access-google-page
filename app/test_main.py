from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_func:
        yield mock_func


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_func:
        yield mock_func


def test_cannot_access_if_connection_or_valid_url_is_true(
        mocked_internet_connection, mocked_valid_url):
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"


def test_cannot_access_if_only_connection(
        mocked_internet_connection, mocked_valid_url):
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("") == "Not accessible"


def test_cannot_access_if_only_valid_url(
        mocked_internet_connection, mocked_valid_url):
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"
