from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    url = "http://www.google.com"

    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(url) == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    url = "http://www.google.com"

    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    url = "http://invalid.google.url"

    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url() -> None:
    url = "http://invalid.google.url"

    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(url) == "Not accessible"
