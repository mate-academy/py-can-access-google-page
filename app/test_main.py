
from app import main


def test_can_access_google_page_when_url_valid_and_internet_available(
    monkeypatch,
):
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: True
    )
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: True
    )

    result = main.can_access_google_page("https://google.com")

    assert result == "Accessible"


def test_can_access_google_page_when_url_invalid(monkeypatch):
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: False
    )
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: True
    )

    result = main.can_access_google_page("https://example.com")

    assert result == "Not accessible"


def test_can_access_google_page_when_no_internet(monkeypatch):
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: True
    )
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: False
    )

    result = main.can_access_google_page("https://google.com")

    assert result == "Not accessible"


def test_can_access_google_page_when_url_invalid_and_no_internet(
    monkeypatch,
):
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: False
    )
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: False
    )

    result = main.can_access_google_page("https://example.com")

    assert result == "Not accessible"
