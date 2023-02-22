from app import main
from app.main import can_access_google_page
from typing import Generator

# write your code here


def test_can_access_google_page_ok(monkeypatch: Generator) -> None:
    valid_url = "www.google.com"

    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(main, "has_internet_connection",
                        mock_has_internet_connection)
    assert can_access_google_page(valid_url) == "Accessible"


def test_can_access_google_page_without_internet_not_ok(
        monkeypatch: Generator) -> None:
    valid_url = "www.google.com"

    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(main, "has_internet_connection",
                        mock_has_internet_connection)
    assert can_access_google_page(valid_url) == "Not accessible"


def test_can_access_google_page_invalid_url_not_ok(
        monkeypatch: Generator) -> None:
    valid_url = "google"

    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(main, "has_internet_connection",
                        mock_has_internet_connection)
    assert can_access_google_page(valid_url) == "Not accessible"
