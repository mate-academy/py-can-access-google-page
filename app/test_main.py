import unittest
from unittest.mock import patch
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
        self.mock_valid_google_url_patcher = patch("app.main.valid_google_url")
        self.mock_valid_google_url = (
            self.mock_valid_google_url_patcher.start())

        self.mock_has_internet_connection_patcher = (
            patch("app.main.has_internet_connection"))
        self.mock_has_internet_connection = (
            self.mock_has_internet_connection_patcher.start())

    def tearDown(self) -> None:
        self.mock_valid_google_url_patcher.stop()
        self.mock_has_internet_connection_patcher.stop()

    def test_can_access_google_page(self) -> None:
        # Mocking the valid_google_url function
        self.mock_valid_google_url.return_value = True

        # Mocking the has_internet_connection
        # function to be within the internet connection window
        self.mock_has_internet_connection.return_value = True

        # Test
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Accessible")

        # Changing the return value of
        # valid_google_url to simulate an invalid url
        self.mock_valid_google_url.return_value = False
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Not accessible")

        # Changing the return value of
        # has_internet_connection to simulate no internet connection
        self.mock_valid_google_url.return_value = True
        self.mock_has_internet_connection.return_value = False
        result = main.can_access_google_page(self.url)
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
