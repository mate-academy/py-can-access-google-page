from app.main import can_access_google_page
from unittest.mock import patch
from typing import Callable


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_accessible_when_url_valid_and_internet_on(
    mock_valid_google_url: Callable,
    mock_has_internet_connection: Callable
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_not_accessible_when_internet_off(
    mock_valid_google_url: Callable,
    mock_has_internet_connection: Callable
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_not_accessible_when_url_invalid(
    mock_valid_google_url: Callable,
    mock_has_internet_connection: Callable
) -> None:
    assert can_access_google_page(
        "https://invalid-url.com"
    ) == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_not_accessible_when_url_invalid_and_internet_off(
    mock_valid_google_url: Callable,
    mock_has_internet_connection: Callable
) -> None:
    assert can_access_google_page(
        "https://invalid-url.com"
    ) == "Not accessible"
