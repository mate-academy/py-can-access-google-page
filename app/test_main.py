from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def valid_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def internet_connection_exists() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection")\
            as mocked_internet_connection:
        yield mocked_internet_connection


def test_valid_url_and_connection_exists(
        valid_url: mock.MagicMock,
        internet_connection_exists: mock.MagicMock) -> None:
    valid_url.return_value = True
    internet_connection_exists.return_value = True
    can_access_google_page("https://www.google.com/")
    valid_url.assert_called_once()
    internet_connection_exists.assert_called_once()
