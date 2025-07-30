import pytest

from app.main import can_access_google_page


def test_can_access_if_both_valid(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("google.com") == "Accessible"


def test_can_access_if_both_invalid(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("google.com") == "Not accessible"


def test_can_access_if_url_invalid(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("google.com") == "Not accessible"


def test_can_access_if_connection_invalid(monkeypatch: pytest.MonkeyPatch)\
        -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("google.com") == "Not accessible"
