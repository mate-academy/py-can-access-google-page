import unittest
from unittest.mock import patch, MagicMock
import datetime
from app import main  # assuming the functions are in main.py


def current_time() -> datetime.datetime:
    return datetime.datetime.now()


main.current_time = current_time


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Setting up the class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tearing down the class")

    def setUp(self) -> None:
        self.url = "https://www.google.com"
        self.mock_requests_get_patcher = patch("app.main.requests.get")
        self.mock_requests_get = self.mock_requests_get_patcher.start()

        self.mock_datetime_now_patcher = patch("app.main.current_time")
        self.mock_datetime_now = self.mock_datetime_now_patcher.start()

    def tearDown(self) -> None:
        self.mock_requests_get_patcher.stop()
        self.mock_datetime_now_patcher.stop()

    def test_can_access_google_page(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        self.mock_requests_get.return_value = mock_response

        # Mocking the current time to be within the internet connection window
        mock_time = datetime.datetime(2022, 1, 1, 10, 0, 0)
        self.mock_datetime_now.return_value = mock_time

        # Test
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Accessible")

        # Changing the status_code to simulate an invalid url
        mock_response.status_code = 404
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Not accessible")

        # Changing the time to simulate no internet connection
        mock_time = datetime.datetime(2022, 1, 1, 23, 0, 0)
        self.mock_datetime_now.return_value = mock_time
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
