
def test_can_access_google_page(monkeypatch: any) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True

    def mock_has_internet_connection() -> bool:
        return True

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
