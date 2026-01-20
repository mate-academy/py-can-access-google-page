from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.fixture
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


def test_everything_works(mocked_internet_connection: None,
                          mocked_valid_google_url: None) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Accessible", "Internet connection and url are available"


def test_no_connection(mocked_internet_connection: None,
                       mocked_valid_google_url: None) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Not accessible", "Internet connection is not available"


def test_invalid_url(mocked_internet_connection: None,
                     mocked_valid_google_url: None) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Not accessible", "URL is not available"


def test_everything_is_not_working(mocked_internet_connection: None,
                                   mocked_valid_google_url: None) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Not accessible", "Internet connection and URL are not available"
