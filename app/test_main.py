
from unittest.mock import patch

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    url = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=True), \
            patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Accessible"

    with patch("app.main.has_internet_connection", return_value=False), \
            patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page(url) == "Not accessible"

    with patch("app.main.has_internet_connection", return_value=True), \
            patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"

    with patch("app.main.has_internet_connection", return_value=False), \
            patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page(url) == "Not accessible"
