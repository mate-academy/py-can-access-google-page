import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connect:
        yield mocked_connect


def test_should_return_accessible(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("url") == "Accessible"


def test_should_return_not_connection(mock_url, mock_connection):
    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"


def test_should_return_invalid_url(mock_url, mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible"


def test_should_return_not_accessible(mock_url, mock_connection):
    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
