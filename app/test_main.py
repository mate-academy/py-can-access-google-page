from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_valid_url_with_internet():
    with mock.patch("app.main.valid_google_url", return_value=True), \
         mock.patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_can_access_google_page_no_internet():
    with mock.patch("app.main.valid_google_url", return_value=True), \
         mock.patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url():
    with mock.patch("app.main.valid_google_url", return_value=False), \
         mock.patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.invalid-url.com")
        assert result == "Not accessible"
