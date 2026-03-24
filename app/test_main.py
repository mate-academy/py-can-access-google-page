from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_when_all_conditions_true() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_google_page_when_no_internet() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_can_access_google_page_when_url_invalid() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
