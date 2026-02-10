import pytest

from app.main import can_access_google_page


def test_valid_url_and_connection_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_valid_google_url(url: str) -> bool:
        return True

    def fake_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", fake_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection
    )
    assert can_access_google_page("https://google.com") == "Accessible"


def test_invalid_url_and_connection_not_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_valid_google_url(url: str) -> bool:
        return False

    def fake_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr("app.main.valid_google_url", fake_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection
    )
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_valid_url_and_connection_not_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_valid_google_url(url: str) -> bool:
        return True

    def fake_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr("app.main.valid_google_url", fake_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection
    )
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_invalid_url_and_connection_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_valid_google_url(url: str) -> bool:
        return False

    def fake_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", fake_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection", fake_has_internet_connection
    )
    assert can_access_google_page("https://google.com") == "Not accessible"
