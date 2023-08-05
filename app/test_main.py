
from app import main


def test_can_access_google_page_with_valid_url_and_internet_connection():
    url = "https://www.google.com"
    assert main.can_access_google_page(url) == "Accessible"


def test_can_access_google_page_with_invalid_url(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)

    url = "https://www.this-url-does-not-exist.com"
    assert main.can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_with_unreachable_url():
    url = "https://www.google.com/nonexistentpage"
    assert main.can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_without_internet_connection(monkeypatch):
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)

    url = "https://www.google.com"
    assert main.can_access_google_page(url) == "Not accessible"
