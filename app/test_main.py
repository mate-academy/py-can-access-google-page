import pytest
from app.main import can_access_google_page

def test_can_access_google_page_success(monkeypatch):
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_no_internet(monkeypatch):
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)  

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_invalid_url(monkeypatch):
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
