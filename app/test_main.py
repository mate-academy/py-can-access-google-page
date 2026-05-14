import pytest

from app import main


def test_can_access_google_page(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_has_internet_connection() -> bool:
        return True

    def mock_valid_google_url(url: str) -> bool:
        return True

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("https://www.google.com") \
        == "Accessible"


def test_cannot_access_without_connection(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_has_internet_connection() -> bool:
        return False

    def mock_valid_google_url(url: str) -> bool:
        return True

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("https://www.google.com") \
        == "Not accessible"


def test_cannot_access_without_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_has_internet_connection() -> bool:
        return True

    def mock_valid_google_url(url: str) -> bool:
        return False

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("https://www.google.com") \
        == "Not accessible"


def test_cannot_access_without_connection_and_valid_url(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_has_internet_connection() -> bool:
        return False

    def mock_valid_google_url(url: str) -> bool:
        return False

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("https://www.google.com") \
        == "Not accessible"
