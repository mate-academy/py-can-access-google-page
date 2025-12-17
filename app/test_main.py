from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible_internet_and_url_valid() -> None:
    url = "https://www.google.com/"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"


def test_can_access_google_page_not_accessible_when_no_internet() -> None:
    url = "https://www.google.com/"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_not_accessible_when_url_invalid() -> None:
    url = "https://www.google.com/"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"
