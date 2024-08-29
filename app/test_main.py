import pytest
from app.main import can_access_google_page
from unittest.mock import patch, MagicMock


@pytest.fixture()
def url() -> str:
    url = "https://Chubur/py-can-access-google-page"
    return url


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_conection(mock_valid_google_url: MagicMock,
                                 mock_has_internet_connection: MagicMock,
                                 url: str) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(url) == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_conection(mock_valid_google_url: MagicMock,
                                   mock_has_internet_connection: MagicMock,
                                   url: str) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_no_conection(mock_valid_google_url: MagicMock,
                                    mock_has_internet_connection: MagicMock,
                                    url: str) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"
