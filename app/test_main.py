from pytest import MonkeyPatch

import app.main


def test_successfully_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    assert (
        app.main.can_access_google_page(
            "https://www.google.com"
        ) == "Accessible"
    ), "The url should be accessible"


def test_not_google_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    assert (
        app.main.can_access_google_page(
            "https://mate.academy"
        ) == "Not accessible"
    ), "The url should not be accessible - wrong url"


def test_not_correct_internet_time(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    assert (
        app.main.can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"
    ), "The url should not be accessible - wrong time"


def test_not_correct_url_and_internet_time(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    assert (
        app.main.can_access_google_page(
            "https://mate.academy"
        ) == "Not accessible"
    ), "The url should not be accessible - wrong url and time"
