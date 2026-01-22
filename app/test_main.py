from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_page:
        yield mock_page


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_url_and_connection_work(mocked_valid_url: None,
                                 mocked_internet_connection: None) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible"


def test_url_does_not_work(mocked_valid_url: None,
                           mocked_internet_connection: None) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_connection_does_not_work(mocked_valid_url: None,
                                  mocked_internet_connection: None) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_nothing_works(mocked_valid_url: None,
                       mocked_internet_connection: None) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"
