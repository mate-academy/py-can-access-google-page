from unittest.mock import patch, MagicMock
import app.main as main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
    mock_connection: MagicMock,
    mock_url: MagicMock
) -> str:
    mock_url.return_value = True
    mock_connection.return_value = True

    result = main.can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection(
    mock_connection: MagicMock,
    mock_url: MagicMock
) -> str:
    mock_url.return_value = True
    mock_connection.return_value = False

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_url(
    mock_connection: MagicMock,
    mock_url: MagicMock
) -> str:
    mock_url.return_value = False
    mock_connection.return_value = True

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url_without_connection(
    mock_connection: MagicMock,
    mock_url: MagicMock
) -> str:
    mock_connection.return_value = False
    mock_url.return_value = False

    result = main.can_access_google_page("wrong_url")
    assert result == "Not accessible"
