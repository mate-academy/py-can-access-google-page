import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_have_good_connection_and_good_url(
        mocked_google_url: str,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("test.com") == "Accessible"


def test_have_bad_connection_and_good_url(
        mocked_google_url: str,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("test.com") == "Not accessible"


def test_have_good_connection_and_bad_url(
        mocked_google_url: str,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("test.com") == "Not accessible"


def test_have_bad_connection_and_bad_url(
        mocked_google_url: str,
        mocked_internet_connection: bool
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("test.com") == "Not accessible"
