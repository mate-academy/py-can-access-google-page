import app.main as func_main
from unittest import mock
import pytest


url = "https://www.google.com/"


@pytest.fixture()
def pytest_connection() -> callable:
    return func_main


def test_connection(pytest_connection: callable) -> None:
    assert pytest_connection.can_access_google_page(url) == "Accessible"
    pytest_connection.has_internet_connection = lambda: False
    assert pytest_connection.can_access_google_page(url) == "Not accessible"
    pytest_connection.has_internet_connection = lambda: True
    pytest_connection.valid_google_url = lambda url: False
    assert pytest_connection.can_access_google_page(url) == "Not accessible"
    pytest_connection.valid_google_url = lambda url: True
    assert pytest_connection.can_access_google_page(url) == "Accessible"


def test_returns_accessible_when_url_valid_and_internet_available() -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        func_main.can_access_google_page(url)
        mock_valid_url.assert_called_once_with(url)
        mock_has_connection.assert_called_once()
