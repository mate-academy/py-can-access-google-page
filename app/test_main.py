import pytest

from app import main
from app.main import can_access_google_page


def test_accessible_if_connection_and_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_not_accessible_if_no_connection_and_no_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_not_accessible_if_only_connection(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_not_accessible_if_only_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
