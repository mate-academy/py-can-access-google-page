from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_internet_connection() -> Mock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.fixture()
def mocked_valid_url() -> Mock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


def test_if_valid_address_and_time(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = True
    assert can_access_google_page("url_address") == "Accessible"


def test_if_valid_address_and_invalid_internet_connection(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = True
    assert can_access_google_page("url_address") == "Not accessible"


def test_if_invalid_address_and_valid_internet_connection(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = False
    assert can_access_google_page("url_address") == "Not accessible"


def test_if_invalid_address_and_invalid_internet_connection(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = False
    assert can_access_google_page("url_address") == "Not accessible"


def test_if_valid_google_url_is_called(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_internet_connection.return_value = True
    can_access_google_page("https://www.google.com/")

    mocked_valid_url.assert_called_once_with(
        "https://www.google.com/"
    )


def test_if_has_internet_connection_called(
        mocked_internet_connection: Mock,
        mocked_valid_url: Mock
) -> None:
    mocked_valid_url.return_value = True
    can_access_google_page("url_address")

    mocked_internet_connection.assert_called_once()
