
from unittest.mock import patch

from app.main import can_access_google_page

url = "https://www.google.com"


def test_page_is_accessible_when_url_is_valid_and_connection_exists() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
            patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"


def test_page_is_not_accessible_when_url_is_invalid() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
            patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"


def test_page_is_not_accessible_when_connection_missing() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
            patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"


def test_page_is_not_accessible_when_request_fails() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
            patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"
