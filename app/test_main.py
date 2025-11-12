from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    patcher = mock.patch("app.main.has_internet_connection")
    mocked = patcher.start()
    yield mocked
    patcher.stop()


@pytest.fixture()
def mocked_valid_url() -> None:
    patcher = mock.patch("app.main.valid_google_url")
    mocked = patcher.start()
    yield mocked
    patcher.stop()


def test_valid_url_and_connection_exists(
        mocked_valid_url: None, mocked_has_internet_connection: None) -> None:
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"
    mocked_valid_url.assert_called_once_with("http://google.com")
    mocked_has_internet_connection.assert_called_once()


def test_invalid_url_and_connection_exists(mocked_valid_url: None,
                                           mocked_has_internet_connection: None
                                           ) -> None:
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://googlee.com") == "Not accessible"
    mocked_valid_url.assert_called_once_with("http://googlee.com")
    mocked_has_internet_connection.assert_called_once()


def test_valid_url_and_connection_lost(mocked_valid_url: None,
                                       mocked_has_internet_connection: None
                                       ) -> None:
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
    mocked_has_internet_connection.assert_called_once()


def test_invalid_url_and_connection_lost(mocked_valid_url: None,
                                         mocked_has_internet_connection: None
                                         ) -> None:
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
    mocked_has_internet_connection.assert_called_once()
