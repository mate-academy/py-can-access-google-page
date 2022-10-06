from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google:
        yield mocked_valid_google


@pytest.fixture
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_internet_doesnt_work(mock_internet_connection: None,
                              mock_valid_google_url: None) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_google_doesnt_work(mock_internet_connection: None,
                            mock_valid_google_url: None) -> None:
    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_connection_work_and_google_valid(mock_internet_connection: None,
                                          mock_valid_google_url: None) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible"
