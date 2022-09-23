import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_return_true_when_url_exists_and_datetime(
        mock_url,
        mock_connection):

    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://github.com/") == "Accessible"


def test_return_false_when_not_datetime_and_url_exists(
        mock_url,
        mock_connection):

    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://github.com/") == "Not accessible"


def test_return_false_when_url_not_exist_and_datetime(
        mock_url,
        mock_connection):

    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://github.com/") == "Not accessible"


def test_return_false_when_not_datetime_and_not_url(
        mock_url,
        mock_connection):

    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://github.com/") == "Not accessible"
