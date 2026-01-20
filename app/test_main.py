from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("http://example.com") == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("http://example.com") == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("http://example.com") == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("http://example.com") == "Not accessible"
