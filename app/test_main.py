import unittest.mock
from unittest.mock import patch
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_url():
    with mock.patch("app.main.valid_google_url") as url:
        yield url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as connection:
        yield connection


def test_connection(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = True
    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_has_not_internet_connection(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = False
    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_not_valid_url(mock_url, mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = True
    result = can_access_google_page("invalid.url")

    assert result == "Not accessible"
