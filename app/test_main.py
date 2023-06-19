from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_can_access_google_page_if_both_true(monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Accessible"


def test_can_access_google_page_if_not_valid(monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"


def test_can_access_google_page_if_no_connection(
        monkeypatch: MonkeyPatch
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"
