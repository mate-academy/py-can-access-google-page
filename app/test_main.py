from _pytest.monkeypatch import MonkeyPatch
import app.main

def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert app.main.can_access_google_page("https://www.google.com") == "Accessible"

def test_cannot_access_if_only_connection(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert app.main.can_access_google_page("https://www.google.com") == "Not accessible"

def test_cannot_access_if_only_valid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert app.main.can_access_google_page("https://www.google.com") == "Not accessible"

def test_cannot_access_if_no_connection_and_invalid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert app.main.can_access_google_page("https://www.google.com") == "Not accessible"
