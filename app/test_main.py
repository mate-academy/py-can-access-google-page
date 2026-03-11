import pytest
from app.main import can_access_google_page


def test_accessible_when_url_valid_and_internet_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_when_no_internet(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_when_url_invalid(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_when_url_invalid_and_no_internet(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"
