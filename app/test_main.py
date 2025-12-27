from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_page:
        yield mock_page


@pytest.fixture()
def mocked_has_connection():
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_all_works(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible"


def test_no_connection(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_not_response(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_all_false(mocked_valid_url, mocked_has_connection):
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"
