from app.main import can_access_google_page
import pytest


def test_can_access_google_page_available(
        monkeypatch: pytest.MonkeyPatch
) -> None:

    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_due_to_internet_connection(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_both_conditions(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
