from app import main
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_page(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert main.can_access_google_page("https://google.com") == "Accessible"


def test_no_internet_connection(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    assert main.can_access_google_page(
        "https://google.com"
    ) == "Not accessible"


def test_url_not_valid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert main.can_access_google_page(
        "https://google.com"
    ) == "Not accessible"
