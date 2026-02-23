from unittest.mock import patch, MagicMock
from app import main


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_connection_and_url_are_valid(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_no_connection(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_is_invalid(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    result = main.can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_no_connection_and_url_is_invalid(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = False

    result = main.can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"
