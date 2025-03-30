import pytest
from app.main import can_access_google_page


def test_accessible_google_page(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_inaccessible_google_page_due_to_invalid_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page(
        "https://invalid-url.com") == "Not accessible"


def test_inaccessible_google_page_due_to_no_internet(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("https://www.google.com") == "Not accessible"
