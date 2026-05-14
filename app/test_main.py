import unittest.mock
from typing import Callable
from app.main import can_access_google_page


@unittest.mock.patch("app.main.valid_google_url")
@unittest.mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet: Callable,
    mock_url: Callable
) -> None:
    mock_url.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@unittest.mock.patch("app.main.valid_google_url")
@unittest.mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet_connection(
    mock_internet: Callable,
    mock_url: Callable
) -> None:
    mock_url.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@unittest.mock.patch("app.main.valid_google_url")
@unittest.mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url(
    mock_internet: Callable,
    mock_url: Callable
) -> None:
    mock_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
