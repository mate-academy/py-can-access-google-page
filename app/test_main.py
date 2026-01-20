from unittest.mock import patch
from app.main import can_access_google_page


def test_access_google_page_with_valid_url_and_internet_connection() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        assert can_access_google_page(
            "https://www.google.com") == "Accessible"


def test_access_google_page_with_invalid_url() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        assert can_access_google_page(
            "https://invalid-url.com") == "Not accessible"


def test_access_google_page_with_no_internet_connection() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        assert can_access_google_page(
            "https://www.google.com") == "Not accessible"
