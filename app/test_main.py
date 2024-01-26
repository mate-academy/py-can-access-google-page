from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
        mock_has_internet: Callable, mock_valid_url: Callable) -> None:
    url = "http://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_not_accessible_due_to_invalid_url(
        mock_has_internet: Callable, mock_valid_url: Callable) -> None:
    url = ""
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible_due_to_no_internet(
        mock_has_internet: Callable, mock_valid_url: Callable) -> None:
    url = "http://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_google_page_due_to_no_internet_and_invalid_url(
        mock_has_internet: Callable, mock_valid_url: Callable) -> None:
    url = ""
    result = can_access_google_page(url)
    assert result == "Not accessible"
