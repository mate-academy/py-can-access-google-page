from app.main import can_access_google_page
from pytest import MonkeyPatch


def test_accessible(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert can_access_google_page("https://google.com") == "Accessible"


def test_not_accessible_no_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_invalid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert can_access_google_page("https://invalid.com") == "Not accessible"


def test_not_accessible_both_fail(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert can_access_google_page("https://invalid.com") == "Not accessible"
