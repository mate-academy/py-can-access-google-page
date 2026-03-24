from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


def test_can_access_google_page_accessible(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: True,
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: True,
    )

    assert can_access_google_page(
        "https://www.google.com",
    ) == "Accessible"


def test_can_access_google_page_invalid_url(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: False,
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: True,
    )

    assert can_access_google_page(
        "https://www.google.com",
    ) == "Not accessible"


def test_can_access_google_page_no_internet(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: True,
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: False,
    )

    assert can_access_google_page(
        "https://www.google.com",
    ) == "Not accessible"
