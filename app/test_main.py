from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_when_url_valid_and_internet_available() -> None:
    # Symuluje sytuację, gdy mamy dostęp do internetu i poprawny URL
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_when_url_invalid() -> None:
    # Symuluje brak poprawnego URL, mimo że internet jest dostępny
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        assert can_access_google_page("https://fake-url.com") == "Not accessible"


def test_not_accessible_when_no_internet() -> None:
    # Symuluje brak internetu, mimo że URL jest poprawny
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_when_url_invalid_and_no_internet() -> None:
    # Symuluje brak internetu i niepoprawny URL jednocześnie
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):
        assert can_access_google_page("https://bad-url.com") == "Not accessible"
