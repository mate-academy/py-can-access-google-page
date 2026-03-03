from _pytest.monkeypatch import MonkeyPatch
from app.main import can_access_google_page


def test_cannot_access_if_only_valid_url(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_cannot_access_if_only_has_connection(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_cannot_access_if_no_connection_and_invalid_url(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_have_access_if_has_connection_and_valid_url(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"
