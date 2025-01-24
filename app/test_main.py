# tests/test_can_access_google_page.py
import pytest
from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_google_page_accessible(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: True
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: True
    )
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_not_valid_url(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: False
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: True
    )
    assert can_access_google_page("invalid_url") == "Not accessible"


def test_can_access_google_page_no_internet(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: True
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: False
    )
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_not_valid_url_and_no_internet(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: False
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: False
    )
    assert can_access_google_page("invalid_url") == "Not accessible"


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_parametrized(
        monkeypatch: MonkeyPatch, valid_url: bool, has_connection: bool,
        expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: valid_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: has_connection
    )
    assert can_access_google_page("test_url") == expected_result
