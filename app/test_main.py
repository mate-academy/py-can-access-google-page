from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url():
    with mock.patch('app.main.valid_google_url') as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture
def mock_has_internet_connection():
    with mock.patch('app.main.has_internet_connection') as mock_has_internet_connection:
        yield mock_has_internet_connection


def test_valid_url_and_connection_exists(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_invalid_url_and_no_connection(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_invalid_url_and_connection_exists(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_valid_url_and_no_connection(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"



def test_functions_was_called(mock_has_internet_connection, mock_valid_google_url):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    can_access_google_page("https://www.google.com")
    mock_valid_google_url.assert_called_with("https://www.google.com")
    mock_has_internet_connection.assert_called()
