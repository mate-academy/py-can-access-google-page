from unittest import mock
from unittest import TestCase
from app.main import can_access_google_page


class TestAccessToGooglePage(TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_return_result_can_access_to_google_page(
            self,
            valid_google_url: mock,
            has_internet_connection: mock
    ) -> None:
        valid_google_url.return_value = True
        has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page(""), "Accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_return_result_when_not_valid_google_url(
            self, mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page(""), "Not accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_return_result_when_not_has_internet_connection(
            self,
            mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page(""), "Not accessible")
