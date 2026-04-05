import pytest
import app.main as main
from app.main import can_access_google_page


def test_access_page_if_has_connection_and_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda _: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_access_page_if_url_is_incorrect(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda _: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_access_page_if_no_connection(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda _: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_access_page_if_no_connection_and_incorrect_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda _: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    assert can_access_google_page("https://www.google.com") == "Not accessible"
