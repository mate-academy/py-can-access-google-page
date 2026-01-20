from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("http://www.google.com") == "Accessible"


def test_can_not_access_google_page_when_url_is_invalid(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_not_access_google_page_when_no_internet_connection(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_not_access_google_page_when_url_is_invalid_and_no_internet_connection(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("http://www.google.com") == "Not accessible"
