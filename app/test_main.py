import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") \
            as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mock_connection:
        yield mock_connection


def test_if_url_and_connection_work(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"


def test_if_url_not_work(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"


def test_if_no_connection(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(" http://google.com") == "Not accessible"


def test_if_all_not_work(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
