from pytest import MonkeyPatch
from app.main import can_access_google_page


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_access_page_if_not_valid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_access_page_if_not_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
