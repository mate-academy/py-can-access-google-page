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
        scenarios = [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible"),
        ]

        for valid_url, internet_connection, expected_result in scenarios:
            self.mock_valid_google_url.return_value = (
                valid_url)
            self.mock_has_internet_connection.return_value = (
                internet_connection)
            result = can_access_google_page("https://www.google.com")
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
