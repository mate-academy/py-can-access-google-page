from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_valid_url_and_internet_connection(
            self,
            mock_connection: bool,
            mock_url: bool
    ) -> None:

        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_invalid_url_and_internet_connection(
            self,
            mock_connection: bool,
            mock_url: bool
    ) -> None:

        result = can_access_google_page("https://bruh.com")
        assert result == "Not accessible"

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_valid_url_but_no_internet_connection(
            self,
            mock_connection: bool,
            mock_url: bool
    ) -> None:

        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_invalid_url_and_no_internet_connection(
            self,
            mock_connection: bool,
            mock_url: bool
    ) -> None:

        result = can_access_google_page("https://oooMaaaGod.com")
        assert result == "Not accessible"
