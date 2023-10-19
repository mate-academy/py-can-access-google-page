from pytest import MonkeyPatch

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @staticmethod
    def func(url: str) -> str:
        return can_access_google_page(url)

    def test_not_valid_url(self, monkeypatch: MonkeyPatch) -> None:
        def mock_valid_google_url(url: str) -> bool:
            return False

        monkeypatch.setattr("app.main.valid_google_url",
                            mock_valid_google_url)

        assert self.func("") == "Not accessible"

    def test_no_internet_connection(self, monkeypatch: MonkeyPatch) -> None:
        def mock_has_internet_connection() -> bool:
            return False

        monkeypatch.setattr("app.main.has_internet_connection",
                            mock_has_internet_connection)

        assert self.func("") == "Not accessible"

    def test_returns_string(self, monkeypatch: MonkeyPatch) -> None:
        def mock_valid_google_url(url: str) -> bool:
            return True

        def mock_has_internet_connection() -> bool:
            return True

        monkeypatch.setattr("app.main.valid_google_url",
                            mock_valid_google_url)
        monkeypatch.setattr("app.main.has_internet_connection",
                            mock_has_internet_connection)

        assert isinstance(self.func("url"), str)

    def test_valid_url_and_has_connection(self,
                                          monkeypatch: MonkeyPatch) -> None:
        def mock_valid_google_url(url: str) -> bool:
            return True

        def mock_has_internet_connection() -> bool:
            return True

        monkeypatch.setattr("app.main.valid_google_url",
                            mock_valid_google_url)
        monkeypatch.setattr("app.main.has_internet_connection",
                            mock_has_internet_connection)

        assert self.func("url") == "Accessible"
