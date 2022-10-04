import pytest
from unittest import mock


from app.main import can_access_google_page


@pytest.fixture
def mock_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_url_is_true_connection_is_true(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"


def test_url_is_true_connection_is_false(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"


def test_url_is_false_connection_is_true(mock_url, mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


def test_url_is_false_connection_is_false(mock_url, mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"
