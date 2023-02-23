from app.main import can_access_google_page
from pytest import MonkeyPatch


def test_should_have_access(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("url") == "Accessible"


def test_should_not_have_access_due_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("url") == "Not accessible"


def test_should_not_have_access_due_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("url") == "Not accessible"


def test_should_not_have_access_at_all(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("url") == "Not accessible"
