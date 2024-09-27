import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mock_connection() -> mock:
    with mock.patch("app.main.has_internet_connection") as mock_has_connection:
        yield mock_has_connection


def test_with_connection(mock_valid_google_url: mock,
                         mock_connection: mock) -> None:
    mock_valid_google_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://google.com/") == "Not accessible"


def test_with_valid_url(mock_valid_google_url: mock,
                        mock_connection: mock) -> None:
    mock_valid_google_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://google.com/") == "Not accessible"


def test_without_connect_and_valid_url(mock_valid_google_url: mock,
                                       mock_connection: mock) -> None:
    mock_valid_google_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://google.com/") == "Not accessible"


def test_with_connect_and_valid_url(mock_valid_google_url: mock,
                                    mock_connection: mock) -> None:
    mock_valid_google_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://google.com/") == "Accessible"
