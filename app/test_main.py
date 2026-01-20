from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def est_accessible_when_url_is_valid_and_connection_exists(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_and_connection_is_invalid(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("//www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_is_invalid_but_connection_exists(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("//www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_exist_but_connection_is_invalid(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("//www.google") == "Not accessible"
