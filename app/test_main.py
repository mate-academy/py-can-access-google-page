from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page(url="https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_invalid_internet_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page(url="https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_invalid_google_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page(url="https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_invalid_connection_and_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    result = can_access_google_page(url="https://www.google.com")
    assert result == "Not accessible"
