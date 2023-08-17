import app.main as main


def test_cant_access_google_page_no_internet(monkeypatch: None) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return False

    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )


def test_cant_access_google_page_invalid_url(monkeypatch: None) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )

    def mock_valid_google_url(url: str) -> bool:
        return False

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("") == "Not accessible"


def test_can_access_google_page(monkeypatch: None) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr(
        main, "has_internet_connection", mock_has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)

    assert main.can_access_google_page("https://google.com") == "Accessible"
    assert (
        main.can_access_google_page("https://www.google.com") == "Accessible"
    )
