from app import main
from unittest.mock import patch


def test_cannot_access_if_connection_or_valid_url_is_true() -> None:
    # tylko jedno z kryteriów prawdziwe -> brak dostępu
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        url = "https://www.google.com"
        result = main.can_access_google_page(url)
        assert result == "Not accessible"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        url = "https://www.google.com"
        result = main.can_access_google_page(url)
        assert result == "Not accessible"


def test_cannot_access_if_only_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        url = "https://www.google.com"
        result = main.can_access_google_page(url)
        assert result == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        url = "https://www.google.com"
        result = main.can_access_google_page(url)
        assert result == "Not accessible"
