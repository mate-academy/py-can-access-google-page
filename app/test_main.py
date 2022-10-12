from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_success_access_google_page(mock_google_url: bool,
                                    mock_internet_connection: bool) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_without_right_url(mock_google_url: bool,
                           mock_internet_connection: bool) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_without_connection(mock_google_url: bool,
                            mock_internet_connection: bool) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_without_connection_and_right_url(
        mock_google_url: bool, mock_internet_connection: bool) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"
