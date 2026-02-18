import pytest
import app.main as main


def test_not_accessible_without_connection(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_not_accessible_with_invalid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_accessible_only_when_both_true(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = main.can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_not_accessible_when_only_url_is_true(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_not_accessible_when_only_connection_is_true(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"
