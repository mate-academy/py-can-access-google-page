from unittest import mock
import app.main


def test_can_access_google_page() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True),\
         mock.patch("app.main.valid_google_url", return_value=False):
        assert app.main.can_access_google_page(
            r"https://www.google.com.ua/"
        ) == "Not accessible"


def test_valid_url() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=False),\
         mock.patch("app.main.valid_google_url", return_value=True):
        assert app.main.can_access_google_page(
            r"https://www.google.com.ua/"
        ) == "Not accessible"


def test_both() -> None:
    with mock.patch("app.main.has_internet_connection", return_value=True),\
         mock.patch("app.main.valid_google_url", return_value=True):
        assert app.main.can_access_google_page(
            r"https://www.google.com.ua/"
        ) == "Accessible"
