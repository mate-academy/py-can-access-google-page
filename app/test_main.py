from unittest import mock
from requests.exceptions import MissingSchema
from app.main import can_access_google_page

import pytest


@pytest.fixture()
def mock_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_should_return_accessible(mock_valid_url, mock_connection):
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://www.youtube.com/") == "Accessible"


def test_should_return_not_accessible(mock_valid_url, mock_connection):
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://www.youtube.com/") ==\
           "Not accessible"


def test_valid_google_url_and_connection_called(mock_valid_url,
                                                mock_connection):
    can_access_google_page("https://www.youtube.com/")
    mock_valid_url.assert_called_once()
    mock_connection.assert_called_once()


def test_raise_missing_schema(mock_connection):
    with pytest.raises(MissingSchema):
        can_access_google_page(23)
