from app.main import can_access_google_page


def test_accessible(monkeypatch: object) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_due_to_invalid_url(monkeypatch: object) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    assert (can_access_google_page("https://www.fakeurl.com")
            == "Not accessible")


def test_not_accessible_due_to_no_connection(monkeypatch: object) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_due_to_both_false(monkeypatch: object) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert (can_access_google_page("https://www.fakeurl.com")
            == "Not accessible")
