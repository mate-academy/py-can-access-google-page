from unittest import TestCase
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page(self,
                                    mock_valid_google_url: mock.Mock,
                                    mock_has_internet_connection: bool
                                    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_not_google_page(self,
                                        mock_valid_google_url: mock.Mock,
                                        mock_has_internet_connection: bool
                                        ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_notconnection(self,
                                      mock_valid_google_url: mock.Mock,
                                      mock_has_internet_connection: bool
                                      ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
