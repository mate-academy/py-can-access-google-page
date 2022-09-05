from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mock_google_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_access_google(mock_google_url, mock_internet_connection):
    mock_google_url.return_value = True
    mock_internet_connection.return_value = True
    access = can_access_google_page("https://www.google.com/")
    assert access == "Accessible"


def test_access_no_connection(mock_google_url, mock_internet_connection):
    mock_google_url.return_value = True
    mock_internet_connection.return_value = False
    access = can_access_google_page("https://www.google.com/")
    assert access == "Not accessible"


def test_access_wrong_url(mock_google_url, mock_internet_connection):
    mock_google_url.return_value = False
    mock_internet_connection.return_value = True
    access = can_access_google_page("https://www.google.com/")
    assert access == "Not accessible"


def test_access_no_connection_no_url(mock_google_url, mock_internet_connection):
    mock_google_url.return_value = False
    mock_internet_connection.return_value = False
    access = can_access_google_page("https://www.google.com/")
    assert access == "Not accessible"
