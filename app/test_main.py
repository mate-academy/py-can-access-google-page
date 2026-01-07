from _pytest.monkeypatch import MonkeyPatch

import app.main

from app.main import can_access_google_page


def test_can_access_google_page_when_url_is_not_valid(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        lambda *args: False
                        )
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        lambda *args: True
                        )

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_when_internet_is_not_accessible(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        lambda *args: True
                        )
    monkeypatch.setattr(app.main
                        , "has_internet_connection",
                        lambda *args: False
                        )

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_when_nothing_accessible(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        lambda *args: False
                        )
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        lambda *args: False
                        )

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_when_everything_accessible(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        lambda *args: True
                        )
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        lambda *args: True
    )

    assert can_access_google_page("https://www.google.com") == "Accessible"
