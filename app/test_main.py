from _pytest.monkeypatch import MonkeyPatch

import app.main as main


def test_accessible_when_url_and_connection_are_valid(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    result = main.can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_not_accessible_whithout_connection(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert main.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_not_accessible_whith_not_valid_url(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert main.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_not_accessible_when_url_and_connection_are_not_valid(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert main.can_access_google_page(
        "https://www.google.com") == "Not accessible"
