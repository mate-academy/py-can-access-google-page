from app.main import can_access_google_page
from typing import Any


def test_can_access_google_page(monkeypatch: Any) -> None:
    def mock_url(url: str) -> bool:
        return True

    def mock_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_internet_connection)
    assert can_access_google_page("https://google.com") == "Accessible"


def test_no_internet_connection(monkeypatch: Any) -> None:
    def mock_url(url: str) -> bool:
        return True

    def mock_internet_connection() -> bool:
        return False

    monkeypatch.setattr("app.main.valid_google_url", mock_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_internet_connection)
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_200_status_code(monkeypatch: Any) -> None:
    def mock_url(url: str) -> bool:
        return False

    def mock_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_internet_connection)
    assert can_access_google_page("https://google.com") == "Not accessible"
