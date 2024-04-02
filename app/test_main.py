import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_functions() -> tuple:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google,
          mock.patch("app.main.has_internet_connection")
            as mock_has_internet_connection):
        yield mock_valid_google, mock_has_internet_connection


def test_can_access_google_page1(mock_functions: tuple) -> None:
    mock_valid_google, mock_has_internet_connection = mock_functions
    mock_valid_google.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("/")
    assert result == "Accessible"


def test_can_access_google_page2(mock_functions: tuple) -> None:
    mock_valid_google, mock_has_internet_connection = mock_functions
    mock_valid_google.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("/1")
    assert result == "Not accessible"


def test_can_access_google_page3(mock_functions: tuple) -> None:
    mock_valid_google, mock_has_internet_connection = mock_functions
    mock_valid_google.return_value = False
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("/1")
    assert result == "Not accessible"


def test_can_access_google_page4(mock_functions: tuple) -> None:
    mock_valid_google, mock_has_internet_connection = mock_functions
    mock_valid_google.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("/1")
    assert result == "Not accessible"
