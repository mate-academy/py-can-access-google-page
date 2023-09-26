import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestGoogleFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_valid_google_url = patch(
            "app.main.valid_google_url").start()
        self.mock_has_internet_connection = patch(
            "app.main.has_internet_connection").start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_can_access_google_page(self) -> None:
        self.mock_valid_google_url.return_value = True
        self.mock_has_internet_connection.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")
        self.mock_valid_google_url.return_value = False
        self.mock_has_internet_connection.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
        self.mock_valid_google_url.return_value = True
        self.mock_has_internet_connection.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
        self.mock_valid_google_url.return_value = False
        self.mock_has_internet_connection.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
