from typing import Callable
from unittest.mock import patch
from app.main import can_access_google_page


url = "http://www.google.com"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_is_accessible(mock_internet: Callable, mock_url: Callable) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page(url) == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_is_not_accessible_because_of_connection(
        mock_internet: Callable,
        mock_url: Callable
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page(url) == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_is_not_accessible_because_of_url(
        mock_internet: Callable,
        mock_url: Callable
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"
