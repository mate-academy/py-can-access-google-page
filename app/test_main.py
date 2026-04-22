import pytest
from app import main


def test_valid_google_url_with_internet_connection(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock valid_google_url to always return True
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    # mock has_internet_connection to always return True
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert main.can_access_google_page("https://google.com") == "Accessible"


def test_invalid_google_url_with_internet_connection(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock valid_google_url to always return False
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    # mock has_internet_connection to always return True
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert main.can_access_google_page("https://google.com") == \
        "Not accessible"


def test_valid_google_url_with_no_internet_connection(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock valid_google_url to always return True
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    # mock has_internet_connection to always return False
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert main.can_access_google_page("https://google.com") == \
        "Not accessible"


def test_invalid_google_url_with_no_internet_connection(
        monkeypatch: pytest.MonkeyPatch) -> None:
    # mock valid_google_url to always return False
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    # mock has_internet_connection to always return False
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert main.can_access_google_page("https://google.com") == \
        "Not accessible"
