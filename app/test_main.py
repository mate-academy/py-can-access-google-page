from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_if_both_true() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("https://google.com") == "Accessible"


def test_not_accessible_if_only_connection() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_if_only_valid_url() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_if_both_false() -> None:
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("https://google.com") == "Not accessible"
