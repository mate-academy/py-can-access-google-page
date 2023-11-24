from unittest import mock, TestCase

from app.main import can_access_google_page


class TestAccessToGooglePage(TestCase):
    def setUp(self) -> None:
        self.url = "https://www.google.com"
        self.valid_url = mock.patch("app.main.valid_google_url")
        self.has_connection = mock.patch("app.main.has_internet_connection")

    def test_access_with_invalid_url(self) -> None:
        with self.valid_url as mock_valid_url:
            mock_valid_url.return_value = False

            assert can_access_google_page(self.url) == "Not accessible"

    def test_without_connection(self) -> None:
        with self.has_connection as mock_has_connection:
            mock_has_connection.return_value = False

            assert can_access_google_page(self.url) == "Not accessible"

    def test_valid_url_and_connection_exists(self) -> None:
        assert can_access_google_page(self.url) == "Accessible"
