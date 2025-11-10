from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture(scope="function")
def mocked_get_url() -> mock:
    with mock.patch("app.main.valid_google_url") as valid_google_url:
        yield valid_google_url


@pytest.fixture(scope="function")
def mocked_get_connection() -> mock:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_connection_check):
        yield mocked_connection_check


def test_valid_url_and_connection_exists(mocked_get_url: mock,
                                         mocked_get_connection: mock) -> None:
    mocked_get_url.return_value = True
    mocked_get_connection.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


def test_url_valid_but_connection_does_not_exists(
        mocked_get_url: mock, mocked_get_connection: mock) -> None:
    mocked_get_url.return_value = True
    mocked_get_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


def test_url_not_valid_but_connection_exists(
        mocked_get_url: mock, mocked_get_connection: mock) -> None:
    mocked_get_url.return_value = False
    mocked_get_connection.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"


def test_both_url_and_connection_return_false(
        mocked_get_url: mock, mocked_get_connection: mock) -> None:
    mocked_get_url.return_value = False
    mocked_get_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"
