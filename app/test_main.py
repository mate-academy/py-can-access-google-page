from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("http://www.google.com") == "Accessible"


def test_cannot_access_google_page_because_first_argument_is_false(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_cannot_access_google_page_because_second_argument_is_false(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_cannot_access_google_page_because_both_arguments_is_false(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    assert can_access_google_page("http://www.google.com") == "Not accessible"
