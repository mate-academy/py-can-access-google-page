from _pytest.monkeypatch import MonkeyPatch
import app.main


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: True)
    result = app.main.can_access_google_page("url")
    assert result == "Accessible"


def test_only_has_internet_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: True)
    result = app.main.can_access_google_page("url")
    assert result == "Not accessible"


def test_only_valid_google_url_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: False)
    result = app.main.can_access_google_page("url")
    assert result == "Not accessible"


def test_both_functions_does_not_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: False)
    result = app.main.can_access_google_page("url")
    assert result == "Not accessible"
