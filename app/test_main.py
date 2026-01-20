from app import main
from unittest.mock import patch


def test_can_access_google_page_all_combinations() -> None:
    url = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        result = main.can_access_google_page(url)
        assert result == "Accessible"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        result = main.can_access_google_page(url)
        assert result == "Not accessible"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        result = main.can_access_google_page(url)
        assert result == "Not accessible"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        result = main.can_access_google_page(url)
        assert result == "Not accessible"
