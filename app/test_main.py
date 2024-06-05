import app.main

def test_should_access_google_page(monkeypatch) -> None:
    monkeypatch.setattr(app.main, 'has_internet_connection', lambda: True)
    monkeypatch.setattr(app.main, 'valid_google_url', lambda url: True)
    assert app.main.can_access_google_page("google.com") == "Accessible"

def test_should_not_access_google_page(monkeypatch) -> None:
    monkeypatch.setattr(app.main, 'has_internet_connection', lambda: True)
    monkeypatch.setattr(app.main, 'valid_google_url', lambda url: False)
    assert app.main.can_access_google_page("google.com") == "Not accessible"

    monkeypatch.setattr(app.main, 'has_internet_connection', lambda: False)
    monkeypatch.setattr(app.main, 'valid_google_url', lambda url: True)
    assert app.main.can_access_google_page("google.com") == "Not accessible"

    monkeypatch.setattr(app.main, 'has_internet_connection', lambda: False)
    monkeypatch.setattr(app.main, 'valid_google_url', lambda url: False)
    assert app.main.can_access_google_page("google.com") == "Not accessible"
