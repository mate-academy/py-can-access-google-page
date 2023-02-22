import pytest
from unittest import mock

from app.main import can_access_google_page

URL = "http//:www.google.com/"


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_func:
        yield mocked_func


@pytest.fixture()
def mocked_has_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_func:
        yield mocked_func


def test_valid_connection_and_url_exist(
        mocked_valid_google_url: mock,
        mocked_has_connection: mock) -> None:

    mocked_valid_google_url.return_value = True
    mocked_has_connection.return_value = True

    assert can_access_google_page(URL) == "Accessible"


def test_invalid_connection_and_valid_url_exist(
        mocked_valid_google_url: mock,
        mocked_has_connection: mock) -> None:

    mocked_valid_google_url.return_value = True
    mocked_has_connection.return_value = False

    assert can_access_google_page(URL) == "Not accessible"


def test_valid_connection_and_invalid_url_exist(
        mocked_valid_google_url: mock,
        mocked_has_connection: mock) -> None:

    mocked_valid_google_url.return_value = False
    mocked_has_connection.return_value = True

    assert can_access_google_page(URL) == "Not accessible"


def test_invalid_connection_and_invalid_url_exist(
        mocked_valid_google_url: mock,
        mocked_has_connection: mock) -> None:

    mocked_valid_google_url.return_value = False
    mocked_has_connection.return_value = False

    assert can_access_google_page(URL) == "Not accessible"
