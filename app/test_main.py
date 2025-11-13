from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_when_valid_url_and_internet_available() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("https://google.com") == "Accessible"


def test_not_accessible_when_url_invalid() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://fake.com"
            ) == "Not accessible"


def test_not_accessible_when_no_internet() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(
                "https://google.com"
            ) == "Not accessible"
