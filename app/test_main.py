from app.main import can_access_google_page


def test_accessible_when_both_conditions_true(monkeypatch):
    calls = []

    def spy_valid_google_url(url):
        calls.append(url)
        return True

    monkeypatch.setattr("app.main.valid_google_url", spy_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"
    assert calls == ["https://www.google.com"]  # Confirm URL was passed


def test_not_accessible_when_no_internet(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_not_accessible_when_invalid_url(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_not_accessible_when_both_false(monkeypatch):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

