from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_google_url_and_connection_exists(
    mock_valid_url: patch, mock_connection: patch
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_google_url_and_connection_exists(
    mock_valid_url: patch, mock_connection: patch
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://invalid.com") == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_google_url_and_no_connection(
    mock_valid_url: patch, mock_connection: patch
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = True
    assert (
        can_access_google_page("https://google.com") == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_google_url_and_no_connection(
    mock_valid_url: patch, mock_connection: patch
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://invalid.com") == "Not accessible"
    )
