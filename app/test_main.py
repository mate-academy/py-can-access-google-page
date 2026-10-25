
from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_no_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://example.com")

    assert result == "Not accessible"
