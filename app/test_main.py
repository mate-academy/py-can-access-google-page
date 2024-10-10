from unittest.mock import patch

from app.main import can_access_google_page


def test_cannot_access_if_only_valid_url() -> None:
    url = "https://www.google.com"

    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page(url)
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    url = "https://www.invalid-url.com"

    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page(url)
        assert result == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url() -> None:
    url = "https://www.invalid-url.com"

    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        result = can_access_google_page(url)
        assert result == "Not accessible"
