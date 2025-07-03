from unittest.mock import patch
from app.main import can_access_google_page
from typing import Any


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_no_connection(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("https://google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False

    result = can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_empty_url_and_connection_exists(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_none_url_and_connection_exists(
        mock_valid_url: bool,
        mock_internet: bool
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page(None)

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_function_calls_dependencies_correctly(
        mock_valid_url: Any,
        mock_internet: Any
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    test_url = "https://google.com"
    result = can_access_google_page(test_url)

    mock_valid_url.assert_called_once_with(test_url)
    mock_internet.assert_called_once()

    assert result == "Accessible"
