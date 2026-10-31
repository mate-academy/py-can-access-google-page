from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_connection.return_value = True
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_when_connection_exists(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_connection.return_value = True
    url = "https://invalid-url.com"
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_when_connection_does_not_exist(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_connection.return_value = False
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_connection_does_not_exist(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_connection.return_value = False
    url = "https://invalid-url.com"
    assert can_access_google_page(url) == "Not accessible"
