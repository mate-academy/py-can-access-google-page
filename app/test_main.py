from typing import Any
from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> Mock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> Mock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_can_access_google_page(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> Any:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("url") == "Accessible"


def test_cannot_access_if_only_connection(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> Any:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible"


def test_cannot_access_if_only_valid_url(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> Any:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"


def test_failed_access_google_page(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock
) -> Any:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
