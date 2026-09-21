import pytest
from unittest.mock import patch, MagicMock
from app import main


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_url_accessible(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Accessible"

@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_url_not_internet_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_url_not_internet_connection_and_invalid_url(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_url_is_invalid_url(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
