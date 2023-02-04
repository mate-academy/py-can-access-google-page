from unittest import mock
from app.main import can_access_google_page


def test_test_main_when_internet_connection_and_valid_url(
) -> None:
    with (mock.patch("app.main.has_internet_connection") as ic,
          mock.patch("app.main.valid_google_url") as url):
        ic.return_value = True
        url.return_value = True
        assert can_access_google_page("http://www.google.com") == "Accessible"


def test_test_main_when_no_valid_url(
) -> None:
    with (mock.patch("app.main.has_internet_connection") as ic,
          mock.patch("app.main.valid_google_url") as url):
        ic.return_value = True
        url.return_value = False
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"


def test_test_main_when_no_internet_connection(
) -> None:
    with (mock.patch("app.main.has_internet_connection") as ic,
          mock.patch("app.main.valid_google_url") as url):
        ic.return_value = False
        url.return_value = True
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"
