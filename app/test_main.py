from app.main import can_access_google_page


def mock_valid_google_url(url: str) -> bool:
    return True


def mock_invalid_google_url(url: str) -> bool:
    return False


def mock_has_internet_connection() -> bool:
    return True


def mock_has_no_internet_connection() -> bool:
    return False


def test_not_accessible_with_only_valid_url(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_no_internet_connection
    )
    assert can_access_google_page("http://google.com") == "Not accessible"


def test_not_accessible_when_only_has_internet_connection(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_invalid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page("http://google.com") == "Not accessible"


def test_accessible_if_valid_url_and_internet_connection(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page("http://google.com") == "Accessible"
