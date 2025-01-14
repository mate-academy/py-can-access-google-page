import pytest
from app import main

def test_cannot_access_if_connection_or_valid_url_is_true(monkeypatch):
    def mock_has_internet_connection():
        return True

    def mock_valid_google_url(url):
        return False

    monkeypatch.setattr(main, "has_internet_connection", mock_has_internet_connection)
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    result = main.can_access_google_page("http://example.com")
    assert result == "Not accessible", (
        "You cannot access page if only one of 'connection' or 'valid url' is True."
    )

def test_cannot_access_if_only_connection(monkeypatch):
    def mock_has_internet_connection():
        return True

    def mock_valid_google_url(url):
        return False

    monkeypatch.setattr(main, "has_internet_connection", mock_has_internet_connection)
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    result = main.can_access_google_page("http://invalid-url.com")
    assert result == "Not accessible", "You cannot access page if only 'connection' is True."

def test_cannot_access_if_only_valid_url(monkeypatch):
    def mock_has_internet_connection():
        return False

    def mock_valid_google_url(url):
        return True

    monkeypatch.setattr(main, "has_internet_connection", mock_has_internet_connection)
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Not accessible", "You cannot access page if only 'valid url' is True."
