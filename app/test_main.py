from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture
def url() -> str:
    return "https://www.google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_not_internet_connection(
        mock_inet: mock, mock_url: mock, url: str) -> None:
    mock_inet.return_value = False
    mock_url.return_value = True

    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_not_valid_google_url(
        mock_inet: mock, mock_url: mock, url: str) -> None:
    mock_inet.return_value = True
    mock_url.return_value = False

    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_inet: mock, mock_url: mock, url: str) -> None:
    mock_inet.return_value = True
    mock_url.return_value = True

    assert can_access_google_page(url) == "Accessible"
