from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.fixture
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture
def mocked_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as internet_connection:
        yield internet_connection


def test_cannot_access_if_only_connection(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock) \
        -> AssertionError:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("a") == "Not accessible"


def test_cannot_access_if_only_valid_url(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock)\
        -> AssertionError:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("a") == "Not accessible"
