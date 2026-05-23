from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible(mock_internet_connection: MagicMock,
                    mock_valid_google_url: MagicMock) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url(mock_internet_connection: MagicMock,
                     mock_valid_google_url: MagicMock) -> None:
    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_internet_connection(mock_internet_connection: MagicMock,
                                mock_valid_google_url: MagicMock) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
