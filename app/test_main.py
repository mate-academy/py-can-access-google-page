from typing import Any

from app.main import can_access_google_page


def test_access_google_page(monkeypatch: Any) -> None:
    def mock_has_internet_connection() -> bool:
        return True

    def mock_valid_google_url(url: str) -> bool:
        return True

    monkeypatch.setattr(
        "app.main.valid_google_url", mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )

    assert can_access_google_page("url") == "Accessible"


def test_not_access_google_page(monkeypatch: Any) -> None:
    def mock_has_internet_connection() -> bool:
        return False

    def mock_valid_google_url(url: str) -> bool:
        return True

    monkeypatch.setattr(
        "app.main.valid_google_url", mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )

    assert can_access_google_page("url") == "Not accessible"
