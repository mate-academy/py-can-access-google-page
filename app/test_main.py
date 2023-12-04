from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_can_access_google_page_with_valid_url_and_connection(mocked_url, mocked_internet_connection) -> None:
    mocked_url.return_value = True
    mocked_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_cannot_access_google_page_with_invalid_url(mocked_url, mocked_internet_connection) -> None:
    mocked_url.return_value = False
    mocked_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_cannot_access_google_page_with_no_internet_connection(mocked_url, mocked_internet_connection) -> None:
    mocked_url.return_value = True
    mocked_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_cannot_access_google_page_with_no_internet_connection_and_invalid_url(mocked_url, mocked_internet_connection) -> None:
    mocked_url.return_value = False
    mocked_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
