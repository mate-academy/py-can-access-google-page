import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_bad_url(
        mock_url: mock, mock_connection: mock) -> None:
    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_bad_connection(
        mock_url: mock, mock_connection: mock) -> None:
    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_bad_url_and_connection(
        mock_url: mock, mock_connection: mock) -> None:
    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_good_url_and_connection(
        mock_url: mock, mock_connection: mock) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
