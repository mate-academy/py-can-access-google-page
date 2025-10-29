from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_is_good(mock_has_internet_connection: Callable,
                        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_is_not_good(mock_has_internet_connection: Callable,
                            mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("//www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_is_not_good_from_one_error(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("//www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_is_not_good_from_another_error(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("//www.google") == "Not accessible"
