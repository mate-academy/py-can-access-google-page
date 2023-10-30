from unittest import mock

from app.main import can_access_google_page

from typing import Callable


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_accessible_google_page(
        valid_google_url: Callable,
        has_internet_connection: Callable
) -> None:
    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_valid_google_page(
        valid_google_url: Callable,
        has_internet_connection: Callable
) -> None:
    result = can_access_google_page("http:////n.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_internet_connection_of_page(
        valid_google_url: Callable,
        has_internet_connection: Callable
) -> None:
    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
