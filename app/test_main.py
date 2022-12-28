import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_url_and_connection_exist(
        mocked_url: callable,
        mocked_connection: callable
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"


def test_url_and_connection_do_not_exist(
        mocked_url: callable,
        mocked_connection: callable
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"


def test_url_do_not_exit_and_connection_exist(
        mocked_url: callable,
        mocked_connection: callable
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


def test_url_exist_and_connection_do_not_exist(
        mocked_url: callable,
        mocked_connection: callable
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"
