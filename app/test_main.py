from unittest import mock
from typing import Any
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_internet_connection(mocked_url,
                             mocked_connection) -> None:
    can_access_google_page("")
    mocked_connection.assert_called_once()


def test_is_validator_work(
        mocked_url,
        mocked_connection
) -> None:
    can_access_google_page("")
    mocked_url.assert_called_once_with("")


def test_can_access_google_page_when_checks_are_good(
        mocked_url,
        mocked_connection
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("") == "Accessible"


def test_can_access_google_page_when_url_is_bed(
    mocked_url,
    mocked_connection
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("") == "Not accessible"


def test_can_access_google_page_when_no_connection(
    mocked_url,
    mocked_connection
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"
