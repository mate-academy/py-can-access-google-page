import unittest
from unittest import mock
from app.main import can_access_google_page


class TestMain(unittest.TestCase):

    @mock.patch("app.main.datetime.datetime")
    @mock.patch("requests.get")
    def test_can_access_google_page(
        self, mock_request: mock.Mock, mock_time: mock.Mock
    ) -> None:
        # Mock the response of requests.get
        mock_request.return_value.status_code = 200
        # Mock the current time to be within the range
        mock_time.now.return_value.hour = 10
        # Test the function
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    def test_not_access_if_only_valid_url(self) -> None:
        # valid_google_url True, aber keine Internetverbindung.
        with mock.patch(
            "app.main.has_internet_connection", return_value=False
        ), mock.patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("https://www.google.com")
            self.assertEqual(result, "Not accessible")

    def test_not_access_if_only_internet_connection(self) -> None:
        # has_internet_connection True, aber valid_google_url False.
        with mock.patch(
            "app.main.has_internet_connection", return_value=True
        ), mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("https://www.google.com")
            self.assertEqual(result, "Not accessible")

    def test_not_access_if_both_false(self) -> None:
        # Beide Bedingungen False.
        with mock.patch(
            "app.main.has_internet_connection", return_value=False
        ), mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("https://www.google.com")
            self.assertEqual(result, "Not accessible")
