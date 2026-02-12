import pytest

from app import main


def test_accessible_when_connection_exists_and_url_is_valid(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)

    assert (
        main.can_access_google_page("https://www.google.com") == "Accessible"
    )


def test_not_accessible_when_connection_exists_and_url_is_not_valid(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)

    assert (
        main.can_access_google_page("https://example.com")
        == "Not accessible"
    )


def test_not_accessible_when_connection_does_not_exist_and_url_is_valid(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)

    assert (
        main.can_access_google_page("https://www.google.com")
        == "Not accessible"
    )


def test_not_accessible_when_connection_does_not_exist_and_url_is_not_valid(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)

    assert (
        main.can_access_google_page("https://example.com")
        == "Not accessible"
    )
