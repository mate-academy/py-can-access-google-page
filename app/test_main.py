from app.main import can_access_google_page

def test_can_access_google_page_accessible(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://not-google.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
