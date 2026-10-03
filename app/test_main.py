from pytest import MonkeyPatch
from app.main import can_access_google_page


def test_valid_url_and_connection_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: True
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: True
    )

    assert can_access_google_page("") == "Accessible"


def test_valid_url_but_no_connection_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: True
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: False
    )

    assert can_access_google_page("") == "Not accessible"


def test_invalid_url_but_connection_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: False
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: True
    )

    assert can_access_google_page("") == "Not accessible"


def test_invalid_url_no_connection_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: False
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: False
    )

    assert can_access_google_page("") == "Not accessible"
