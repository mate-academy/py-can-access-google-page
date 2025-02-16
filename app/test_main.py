import pytest
import app.main as main


def test_can_access_google_page_accessible(
        monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection)

    assert main.can_access_google_page(
        "http://www.google.com") == "Accessible"


def test_can_access_google_page_not_accessible_due_to_no_internet(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection)

    assert main.can_access_google_page(
        "http://www.google.com") == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection)

    assert main.can_access_google_page(
        "http://www.invalidurl.com") == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_both(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection)

    assert main.can_access_google_page(
        "http://www.invalidurl.com") == "Not accessible"


def test_cannot_access_if_only_valid_url(
        monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection)

    result = main.can_access_google_page("http://www.google.com")
    assert result == "Not accessible", (
        "You cannot access page if only 'valid url' is True."
    )
