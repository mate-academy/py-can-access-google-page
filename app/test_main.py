from app.main import can_access_google_page


test_url = "https://www.google.com"


def test_accessible_when_all_conditions_met(monkeypatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert can_access_google_page(test_url) == "Accessible"


def test_not_accessible_when_no_internet(monkeypatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    assert can_access_google_page(test_url) == "Not accessible"


def test_not_accessible_when_invalid_url(monkeypatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert can_access_google_page(test_url) == "Not accessible"
