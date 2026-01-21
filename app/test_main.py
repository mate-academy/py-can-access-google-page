from app.main import can_access_google_page
from unittest import mock


def test_accessible_when_url_valid_and_internet_available() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True), \
         mock.patch("app.main.has_internet_connection", return_value=True):
        assert (
            can_access_google_page("https://google.com") == "Accessible"
        ), "Not accessible"


def test_invalid_url_but_has_internet() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False), \
         mock.patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("https://fake.com") == "Not accessible"


def test_valid_url_but_no_internet() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True), \
         mock.patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page("https://fake.com") == "Not accessible"
