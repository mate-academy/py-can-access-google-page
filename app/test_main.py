from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = True
        yield mocked_url


@pytest.fixture
def mock_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        mocked_connection.return_value = True
        yield mocked_connection


def test_when_valid_url_and_has_connection(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    assert can_access_google_page("/") == "Accessible"


def test_func_was_called_once(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    can_access_google_page("/")
    mock_valid_google_url.assert_called_once_with("/")
    mock_has_internet_connection.assert_called_once()


def test_return_not_accessible(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    assert can_access_google_page("/") == "Not accessible"

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("/") == "Not accessible"
