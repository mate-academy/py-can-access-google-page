from unittest import mock
from .main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True), \
         mock.patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://www.google.com")

        assert result == "Accessible"


def test_can_access_google_page_not_accessible_when_url_invalid() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True), \
         mock.patch("app.main.valid_google_url", return_value=False):

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"


def test_can_access_google_page_not_accessible_when_no_internet() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False), \
         mock.patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
