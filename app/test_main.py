import pytest
from app.main import can_access_google_page


def test_can_access_google_page_when_valid_and_connected(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    # Mocking valid_google_url to return True
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    # Mocking has_internet_connection to return True
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_when_valid_but_not_connected(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    # Mocking valid_google_url to return True
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    # Mocking has_internet_connection to return False
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_when_not_valid_but_connected(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    # Mocking valid_google_url to return False
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    # Mocking has_internet_connection to return True
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
