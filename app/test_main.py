from unittest.mock import Mock
import app.main as main


def test_accessible_when_both_true(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", Mock(return_value=True))
    monkeypatch.setattr(main, "has_internet_connection", Mock(return_value=True))

    result = main.can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_not_accessible_if_only_connection_true(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", Mock(return_value=False))
    monkeypatch.setattr(main, "has_internet_connection", Mock(return_value=True))

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_not_accessible_if_only_valid_url_true(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", Mock(return_value=True))
    monkeypatch.setattr(main, "has_internet_connection", Mock(return_value=False))

    result = main.can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_not_accessible_if_both_false(monkeypatch):
    monkeypatch.setattr(main, "valid_google_url", Mock(return_value=False))
    monkeypatch.setattr(main, "has_internet_connection", Mock(return_value=False))

    result = main.can_access_google_page("https://bad.com")
    assert result == "Not accessible"
