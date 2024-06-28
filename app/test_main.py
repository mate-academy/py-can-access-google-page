from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        assert can_access_google_page(
            "http://www.google.com") == "Accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        assert can_access_google_page(
            "http://www.invalid-url.com") == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_no_internet() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_both() -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False
        assert can_access_google_page(
            "http://www.invalid-url.com") == "Not accessible"
