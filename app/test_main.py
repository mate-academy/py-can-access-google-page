from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_can_access_page_when_url_valid_and_connection_exists(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("valid_url") == "Accessible"


def test_cannot_access_if_only_valid_url(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("valid_url") == "Not accessible"


def test_cannot_access_if_only_connection(
        mocked_valid_url: mock.MagicMock,
        mocked_connection: mock.MagicMock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("valid_url") == "Not accessible"
