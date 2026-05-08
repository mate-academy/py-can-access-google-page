from unittest.mock import patch
import app.main as main


def test_accessible() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url", return_value=True):
            assert main.can_access_google_page(
                "https://google.com"
            ) == "Accessible"


def test_no_internet() -> None:
    with patch("app.main.has_internet_connection", return_value=False):
        with patch("app.main.valid_google_url", return_value=True):
            assert main.can_access_google_page(
                "https://google.com"
            ) == "Not accessible"


def test_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=True):
        with patch("app.main.valid_google_url", return_value=False):
            assert main.can_access_google_page(
                "https://invalid.com"
            ) == "Not accessible"


def test_no_internet_and_invalid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False):
        with patch("app.main.valid_google_url", return_value=False):
            assert main.can_access_google_page(
                "https://invalid.com"
            ) == "Not accessible"
