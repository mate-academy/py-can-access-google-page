from _pytest.monkeypatch import MonkeyPatch
import app.main


def test_valid_google_url(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)


def test_has_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda url: True)


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert (app.main.can_access_google_page("https://www.google.com")
            == "Accessible")
