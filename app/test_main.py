from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_test_url:
        yield mocked_test_url


@pytest.fixture()
def mocked_connection():
    with mock.patch("app.main.has_internet_connection") as \
            mocked_test_connection:
        yield mocked_test_connection


def test_access_if_url_is_valid_and_connection_is_worked(
        mocked_url,
        mocked_connection
):
    mocked_url.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page(mocked_url) == "Accessible"


def test_not_accessible_if_url_is_valid_but_connection_is_not_worked(
        mocked_url,
        mocked_connection
):
    mocked_url.return_value = True
    mocked_connection.return_value = False

    assert can_access_google_page(mocked_url) == "Not accessible"


def test_not_accessible_if_url_is_not_valid_but_connection_is_worked(
        mocked_url,
        mocked_connection
):
    mocked_url.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page(mocked_url) == "Not accessible"


def test_not_accessible_if_url_is_not_valid_and_connection_is_not_worked(
        mocked_url,
        mocked_connection
):
    mocked_url.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page(mocked_url) == "Not accessible"
