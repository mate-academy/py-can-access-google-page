from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_with_valid_url_and_internet_connection(
        mock_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_with_invalid_url_and_internet_connection(
        mock_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://Mate.com")

    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_with_valid_url_and_no_internet_connection(
        mock_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
