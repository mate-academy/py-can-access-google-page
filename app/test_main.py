from pytest import fixture
from unittest import mock

from app.main import can_access_google_page


@fixture()
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_test_url:
        yield mocked_test_url


@fixture()
def mocked_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_test_connection:
        yield mocked_test_connection


def test_return_not_accessible_if_url_is_invalid(
        mocked_url,
        mocked_connection) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page(None) == "Not accessible"


def test_return_not_accessible_if_no_connection(
        mocked_url,
        mocked_connection) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page(None) == "Not accessible"


def test_return_accessible_if_url_and_connection(
        mocked_url,
        mocked_connection) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page(None) == "Accessible"


