import pytest
import app.main as main


def test_accessible(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: True,
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: True,
    )

    assert main.can_access_google_page("https://google.com") == "Accessible"


def test_no_internet(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: False,
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: True,
    )

    assert main.can_access_google_page(
        "https://google.com"
    ) == "Not accessible"


def test_invalid_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: True,
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: False,
    )

    assert main.can_access_google_page(
        "https://example.com"
    ) == "Not accessible"


def test_no_internet_and_invalid_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: False,
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: False,
    )

    assert main.can_access_google_page(
        "https://example.com"
    ) == "Not accessible"
