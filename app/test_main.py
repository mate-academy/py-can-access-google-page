from app import main
from pytest import MonkeyPatch


def test_accessible_if_url_is_valid_and_connection_exists(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_not_accessible_if_url_is_invalid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://not-google.com")

    assert result == "Not accessible"


def test_not_accessible_if_connection_does_not_exist(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_not_accessible_if_url_is_invalid_and_connection_does_not_exist(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://not-google.com")

    assert result == "Not accessible"
