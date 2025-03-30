import pytest
from app.main import can_access_google_page


def fake_valid_google_url(url: str) -> bool:
    return url == "https://www.google.com"


def fake_has_internet_connection_true() -> bool:
    return True


def fake_has_internet_connection_false() -> bool:
    return False


def test_can_access_google_page_accessible(
        monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", fake_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection_true
    )
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_no_internet(
        monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", fake_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection_false
    )
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_invalid_url(
        monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", fake_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection_true
    )
    result = can_access_google_page("https://www.notgoogle.com")
    assert result == "Not accessible"
