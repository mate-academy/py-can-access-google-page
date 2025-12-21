import pytest
import app.main as main


def test_accessible_google_page(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_invalid_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://not-google.com")

    assert result == "Not accessible"


def test_no_internet_connection(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_invalid_url_and_no_internet(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://not-google.com")

    assert result == "Not accessible"
