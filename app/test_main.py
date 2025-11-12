from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


VALID_GOOGLE_URL = "https://www.google.com"
INVALID_URL = "https://invalid-url.com"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_accessible_when_url_valid_and_has_connection(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock
) -> None:
    """Should return 'Accessible' when URL is valid and connection exists"""
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page(VALID_GOOGLE_URL)

    assert result == "Accessible"
    mock_valid_url.assert_called_once_with(VALID_GOOGLE_URL)
    mock_has_connection.assert_called_once()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_url_invalid_and_has_connection(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock
) -> None:
    """Should return 'Not accessible' when URL is invalid despite connection"""
    mock_has_connection.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page(INVALID_URL)

    assert result == "Not accessible"
    mock_valid_url.assert_called_once_with(INVALID_URL)
    mock_has_connection.assert_called_once()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_url_valid_but_no_connection(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock
) -> None:
    """Should return 'Not accessible' when URL is valid but no connection"""
    mock_has_connection.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
    mock_has_connection.assert_called_once()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_returns_not_accessible_when_url_invalid_and_no_connection(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock
) -> None:
    """
        Should return 'Not accessible' when both URL
        invalid and no connection
    """
    mock_has_connection.return_value = False
    mock_valid_url.return_value = False

    result = can_access_google_page(INVALID_URL)

    assert result == "Not accessible"
    mock_has_connection.assert_called_once()


@pytest.mark.parametrize("test_url", [
    "https://google.com",
    "http://www.google.com",
    "https://www.google.com/search",
    ""
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_passes_url_correctly_to_valid_google_url(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock,
    test_url: str
) -> None:
    """Should pass the exact URL parameter to valid_google_url function"""
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True

    can_access_google_page(test_url)

    mock_valid_url.assert_called_once_with(test_url)


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_checks_connection_before_validating_url(
    mock_has_connection: MagicMock,
    mock_valid_url: MagicMock
) -> None:
    """Should check internet connection before validating URL for efficiency"""
    mock_has_connection.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page(VALID_GOOGLE_URL)

    assert result == "Not accessible"
    mock_has_connection.assert_called_once()
