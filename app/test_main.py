from unittest.mock import patch, Mock
from typing import Tuple
import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_access_dependencies() -> Tuple[Mock, Mock]:
    with patch("app.main.has_internet_connection") as mock_has_internet, \
         patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_has_internet, mock_valid_url


def test_can_access_google_page_accessible(mock_access_dependencies:
                                           Tuple[Mock, Mock]) -> None:
    mock_has_internet, mock_valid_url = mock_access_dependencies

    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"
    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com")


def test_can_access_google_page_no_internet(mock_access_dependencies:
                                            Tuple[Mock, Mock]) -> None:
    mock_has_internet, mock_valid_url = mock_access_dependencies

    mock_has_internet.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
    mock_has_internet.assert_called_once()
    mock_valid_url.assert_not_called()


def test_can_access_google_page_invalid_url(mock_access_dependencies:
                                            Tuple[Mock, Mock]) -> None:
    mock_has_internet, mock_valid_url = mock_access_dependencies

    mock_has_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com")
