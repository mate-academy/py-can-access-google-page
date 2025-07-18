from unittest.mock import MagicMock

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection() -> MagicMock :
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.fixture()
def mocked_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


def test_access_page_with_no_url(
        mocked_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_access_page_with_no_connection(
        mocked_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_access_page_with_url_and_connection(
        mocked_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


def test_access_page_with_no_url_and_connection(
        mocked_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
