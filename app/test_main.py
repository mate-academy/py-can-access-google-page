from unittest.mock import patch

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    def test_valid_url_and_exists_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=True),
            patch("app.main.has_internet_connection", return_value=True)
        ):
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"

    def test_valid_url_but_not_exists_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=True),
            patch("app.main.has_internet_connection", return_value=False)
        ):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"

    def test_invalid_url_but_exists_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=False),
            patch("app.main.has_internet_connection", return_value=True)
        ):
            result = can_access_google_page("https://www.mock.com")
            assert result == "Not accessible"

    def test_invalid_url_and_not_exists_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=False),
            patch("app.main.has_internet_connection", return_value=False)
        ):
            result = can_access_google_page("https://www.mock.com")
            assert result == "Not accessible"
