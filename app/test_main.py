import app.main

from app.main import can_access_google_page


def test_if_it_works(monkeypatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True


    def mock_has_internet_connection() -> bool:
        return True


    def mock_checker(*args, **kwargs) -> bool:
        return True


    monkeypatch.setattr(app.main, "valid_google_url", mock_checker)
    monkeypatch.setattr(app.main, "has_internet_connection", mock_checker)

    assert can_access_google_page("https://google.com") == "Accessible"
