from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_google_page_accessible(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_can_access_google_page_no_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_can_access_google_page_invalid_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
