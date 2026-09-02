from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_has_internet(mock_url: str, mock_connection: str) \
        -> None:
    mock_url.return_value = True
    mock_connection.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_has_internet(mock_url: str, mock_connection: str)\
        -> None:
    mock_url.return_value = False
    mock_connection.return_value = True

    result = can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_no_internet(mock_url: str, mock_connection: str) \
        -> None:
    mock_url.return_value = True
    mock_connection.return_value = False

    result = can_access_google_page("https://google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_no_internet(mock_url: str, mock_connection: str) \
        -> None:
    mock_url.return_value = False
    mock_connection.return_value = False

    result = can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"
