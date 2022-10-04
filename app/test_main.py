import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_google_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_google_page_true(mocked_google_url, mocked_internet_connection):
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page(100) == "Accessible"


def test_google_page_false(mocked_google_url, mocked_internet_connection):
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page(400) == "Not accessible"
