import pytest
import app.main as main


def test_should_return_accessible_when_url_valid_and_internet_available(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert main.can_access_google_page("https://google.com") == "Accessible"


def test_should_return_not_accessible_when_url_invalid(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert main.can_access_google_page("invalid_url") == "Not accessible"


def test_should_return_not_accessible_when_no_internet(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    assert main.can_access_google_page(
        "https://google.com"
    ) == "Not accessible"
