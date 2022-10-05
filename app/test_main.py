from app.main import can_access_google_page

from unittest import mock

import pytest


@pytest.fixture()
def mock_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_valid_url_and_connection_exists(mock_valid_url, mock_connection):
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible"


def test_not_valid_url_and_connection_exists(mock_valid_url, mock_connection):
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_valid_url_and_not_connection_exists(mock_valid_url, mock_connection):
    mock_valid_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"


def test_not_valid_url_and_not_connection_exists(
    mock_valid_url,
    mock_connection
):
    mock_valid_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible"
