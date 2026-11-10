import pytest

from app.main import can_access_google_page


def test_can_access_google_page(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url",
                        mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_has_internet_connection)

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_not_valid_google_url(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url",
                        mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_has_internet_connection)

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_no_internet_connection(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr("app.main.valid_google_url",
                        mock_valid_google_url)
    monkeypatch.setattr("app.main.has_internet_connection",
                        mock_has_internet_connection)

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
