import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock.MagicMock:
    with (mock.patch("app.main.valid_google_url")
          as mock_google_url):
        yield mock_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> mock.MagicMock:
    with (mock.patch("app.main.has_internet_connection")
          as mock_internet_connection):
        yield mock_internet_connection


def test_has_no_internet_connection(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_cannot_access_google_url(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"
