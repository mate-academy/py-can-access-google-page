from app import main
import pytest


def test_accessible_when_valid_url_and_has_connection(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert (
        main.can_access_google_page("https://google.com")
        == "Accessible"
    )


def test_not_accessible_when_valid_url_but_no_connection(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


def test_not_accessible_when_invalid_url_but_has_connection(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


def test_not_accessible_when_invalid_url_and_no_connection(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )
