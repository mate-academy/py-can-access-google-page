import app.main
from app.main import can_access_google_page


def test_url_true_connection_true(monkeypatch: any) -> None:
    url1 = "https://www.google.com"

    def mock_valid_google_url(url: str = url1) -> bool:
        return True
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        mock_valid_google_url
    )

    def mock_has_internet_connection() -> bool:
        return True
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(url1) == "Accessible"


def test_url_false_connection_false(monkeypatch: any) -> None:
    url1 = "https://www.google.com"

    def mock_valid_google_url(url: str = url1) -> bool:
        return False
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        mock_valid_google_url
    )

    def mock_has_internet_connection() -> bool:
        return False
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(url1) == "Not accessible"


def test_url_true_connection_false(monkeypatch: any) -> None:
    url1 = "https://www.google.com"

    def mock_valid_google_url(url: str = url1) -> bool:
        return True
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        mock_valid_google_url
    )

    def mock_has_internet_connection() -> bool:
        return False
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(url1) == "Not accessible"


def test_url_false_connection_true(monkeypatch: any) -> None:
    url1 = "https://www.google.com"

    def mock_valid_google_url(url: str = url1) -> bool:
        return False
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        mock_valid_google_url
    )

    def mock_has_internet_connection() -> bool:
        return True
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(url1) == "Not accessible"
