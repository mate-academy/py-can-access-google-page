from typing import Generator

from _pytest.monkeypatch import MonkeyPatch

import app
from app.main import can_access_google_page


def test_can_access_google_page(
        monkeypatch: Generator["MonkeyPatch", None, None]
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(app.main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        mock_has_internet_connection)

    assert can_access_google_page("uri") == "Accessible"


def test_cant_access_google_page_no_connection(
        monkeypatch: Generator["MonkeyPatch", None, None]
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(app.main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        mock_has_internet_connection)

    assert can_access_google_page("uri") == "Not accessible"


def test_cant_access_google_page_invalid_uri(
        monkeypatch: Generator["MonkeyPatch", None, None]
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(app.main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        mock_has_internet_connection)

    assert can_access_google_page("uri") == "Not accessible"


def test_cant_access_google_page_invalid_uri_no_connection(
        monkeypatch: Generator["MonkeyPatch", None, None]
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(app.main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        mock_has_internet_connection)

    assert can_access_google_page("uri") == "Not accessible"
