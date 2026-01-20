from app import main
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_when_url_valid_and_internet(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_cannot_access_when_url_invalid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    result = main.can_access_google_page("https://fake-url.com")
    assert result == "Not accessible"


def test_cannot_access_when_no_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_cannot_access_when_both_invalid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    result = main.can_access_google_page("https://fake-url.com")
    assert result == "Not accessible"
