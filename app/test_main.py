from unittest.mock import patch
from app.main import can_access_google_page
from pytest import MonkeyPatch


# Example of a corrected test case
def test_cannot_access_if_only_valid_url(monkeypatch: MonkeyPatch) -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):
        # Directly test the behavior of `can_access_google_page`
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible", "You cannot access page"


def test_cannot_access_if_only_connection() -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):
        # Directly test the behavior of `can_access_google_page`
        result = can_access_google_page("https://notgoogle.com")
        assert result == "Not accessible", "You cannot access the page"
