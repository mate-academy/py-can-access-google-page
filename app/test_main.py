from typing import Callable
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(mock_internet: Callable,
                                           mock_valid_url: Callable
                                           ) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible(mock_internet: Callable,
                                               mock_valid_url: Callable
                                               ) -> None:
    # Case 1: internet OFF
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"

    # Case 2: valid url is False
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
