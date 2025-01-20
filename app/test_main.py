from unittest import mock, TestCase

from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):
    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_has_not_internet_connection(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_has_not_valid_google_url(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ) -> None:
        result = can_access_google_page("htt://www_google_com")
        assert result == "Not accessible"
