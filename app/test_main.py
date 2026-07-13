from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page
from app import main


def test_if_url_and_internet_true(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_if_url_true_and_internet_false(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_if_url_false_and_internet_true(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_if_url_and_internet_false(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"
