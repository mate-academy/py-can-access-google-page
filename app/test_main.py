from _pytest.monkeypatch import MonkeyPatch
from app.main import can_access_google_page


def test_can_access_google_page_accessible(monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url() -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection)

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url(
        monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url() -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection)

    result = can_access_google_page("https://www.invalid_url.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_loss_internet_connection(
        monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url() -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection)

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
