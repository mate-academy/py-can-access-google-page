import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_func:
        mocked_func.return_value = True
        yield mocked_func


@pytest.fixture()
def mocked_has_internet_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_func:
        mocked_func.return_value = True
        yield mocked_func


def test_valid_url_has_internet_connection(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock
) -> None:
    result = can_access_google_page("www.google.com")
    assert result == "Accessible"


def test_cannot_access_with_invalid_google_url(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock
) -> None:
    mocked_valid_google_url.return_value = False
    result = can_access_google_page("www.google.com")
    assert result == "Not accessible"


def test_cannot_access_without_internet_connection(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock
) -> None:
    mocked_has_internet_connection.return_value = False
    result = can_access_google_page("www.google.com")
    assert result == "Not accessible"
