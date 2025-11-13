from app import main


def test_accessible(monkeypatch):
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    assert main.can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_no_internet(monkeypatch):
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    assert main.can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_invalid_url(monkeypatch):
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    assert main.can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_both_false(monkeypatch):
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    assert main.can_access_google_page("https://www.google.com") == "Not accessible"

