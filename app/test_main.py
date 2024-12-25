from app.main import can_access_google_page

from unittest import TestCase, mock


class TestCanAccessGooglePage(TestCase):

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_accessible(
            self,
            mock_valid_url: bool,
            mock_internet: bool
    ) -> None:
        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_invalid_url(
            self,
            mock_valid_url: bool,
            mock_internet: bool
    ) -> None:
        result = can_access_google_page("http://www.invalidurl.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_google_page_no_internet_connection(
            self,
            mock_valid_url: bool,
            mock_internet: bool
    ) -> None:
        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_google_page_no_internet_invalid_url(
            self,
            mock_valid_url: bool,
            mock_internet: bool
    ) -> None:
        result = can_access_google_page("http://www.invalidurl.com")
        self.assertEqual(result, "Not accessible")
