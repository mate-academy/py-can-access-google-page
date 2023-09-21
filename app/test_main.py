from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_time_and_url(internet: Callable,
                            google_valid: Callable) -> None:
    internet.return_value = True
    google_valid.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_time_valid_url(internet: Callable,
                                google_valid: Callable) -> None:
    internet.return_value = False
    google_valid.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_time_invalid_url(internet: Callable,
                                google_valid: Callable) -> None:
    internet.return_value = True
    google_valid.return_value = False
    assert (can_access_google_page("https://www.google.com/")
           == "Not accessible")
