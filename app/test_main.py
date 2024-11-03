from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_page() -> None:
    with (patch("app.main.has_internet_connection", return_value=True),
          patch("app.main.valid_google_url", return_value=True)):
        result = can_access_google_page("http://www.google.com")
        assert result == "Accessible"


def test_not_accessible_no_internet() -> None:
    with (patch("app.main.has_internet_connection", return_value=False),
          patch("app.main.valid_google_url", return_value=True)):
        result = can_access_google_page("http://www.google.com")
        assert result == "Not accessible"


def test_not_accessible_invalid_url() -> None:
    with (patch("app.main.has_internet_connection", return_value=True),
          patch("app.main.valid_google_url", return_valur=True)):
        result = can_access_google_page("http://www.google.com")
        assert result == "Not accessible"
