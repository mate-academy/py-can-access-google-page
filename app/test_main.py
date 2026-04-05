from pytest import MonkeyPatch
from app.main import can_access_google_page


url = "https://google.com"


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda x: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    result = can_access_google_page(url)
    assert result == "Accessible"


def test_no_access_invalid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda x: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    result = can_access_google_page(url)
    assert result == "Not accessible"


def test_no_internet_valid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda x: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    result = can_access_google_page(url)
    assert result == "Not accessible"


def test_no_internet_invalid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda x: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    result = can_access_google_page(url)
    assert result == "Not accessible"
