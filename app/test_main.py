from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_cannot_access_google_page_invalid_url(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert (
        can_access_google_page("https://www.goo!gle.com") == "Not accessible"
    )


def test_has_not_internet_connection(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_invalid_url_and_has_not_connection(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.goole.com") == "Not accessible"
