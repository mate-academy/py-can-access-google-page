from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page_with_both_true() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("http://google.com") == "Accessible"


def test_can_access_google_page_with_conection_false() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page("http://google.com") == "Not accessible"


def test_can_access_google_page_with_url_false() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("http://google.com") == "Not accessible"


def test_can_access_google_page_with_both_false() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        with mock.patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page("http://google.com") == "Not accessible"
