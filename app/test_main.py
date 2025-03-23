from unittest import mock
from app import main


def test_can_access_google_page_when_internet_and_url_are_valid() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True), \
         mock.patch("app.main.valid_google_url", return_value=True):
        result = main.can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_cannot_access_google_page_when_no_internet() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False), \
         mock.patch("app.main.valid_google_url", return_value=True):
        result = main.can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_cannot_access_google_page_when_url_is_invalid() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True), \
         mock.patch("app.main.valid_google_url", return_value=False):
        result = main.can_access_google_page("https://fake-google.com")
        assert result == "Not accessible"


def test_cannot_access_google_page_when_no_internet_and_url_is_invalid() \
        -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False), \
         mock.patch("app.main.valid_google_url", return_value=False):
        result = main.can_access_google_page("https://fake-google.com")
        assert result == "Not accessible"
