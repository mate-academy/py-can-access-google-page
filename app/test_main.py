from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible(
        mock_connection: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_connection(
        mock_connection: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url(
        mock_connection: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = False
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_no_connection_invalid_url(
        mock_connection: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = False
    result = can_access_google_page("https://other.com")
    assert result == "Not accessible"
