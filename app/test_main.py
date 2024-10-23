from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_should_access_if_has_internet_connection_and_valid_url(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("test") == "Accessible"


def test_should_no_access_if_not_internet_connection(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("test") == "Not accessible"


def test_should_no_access_if_not_valid_url(mocked_url, mocked_connection):
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("test") == "Not accessible"