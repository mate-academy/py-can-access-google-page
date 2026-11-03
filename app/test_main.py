from pytest import MonkeyPatch

from app import main


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
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


def test_can_access_google_page_without_internet(
    monkeypatch: MonkeyPatch,
) -> None:
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
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )


def test_can_access_google_page_without_valid_url(
    monkeypatch: MonkeyPatch,
) -> None:
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
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )


def test_can_access_google_page_without_internet_and_valid_url(
    monkeypatch: MonkeyPatch,
) -> None:
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
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )
