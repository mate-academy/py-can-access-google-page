from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_internet(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url(mock_internet: MagicMock, mock_url: MagicMock) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://invalid.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_internet_and_invalid_url(
        mock_internet: MagicMock,
        mock_url: MagicMock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False
    assert can_access_google_page("https://invalid.com") == "Not accessible"
