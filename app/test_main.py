from unittest.mock import patch

from app import main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_has_internet_connection, mock_valid_google_url
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
    mock_has_internet_connection, mock_valid_google_url
):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
    mock_has_internet_connection, mock_valid_google_url
):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = main.can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url_and_no_internet(
    mock_has_internet_connection, mock_valid_google_url
):
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    result = main.can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"
