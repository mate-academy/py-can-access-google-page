import unittest
from unittest.mock import patch
from datetime import datetime
from app.main import can_access_google_page


class TestGoogleFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_datetime = patch("datetime.datetime").start()
        self.mock_get = patch("requests.get").start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_can_access_google_page(self) -> None:
        self.mock_datetime.now.return_value = datetime(2023, 9, 25, 8, 0, 0)
        self.mock_get.return_value.status_code = 200
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")
        self.mock_get.return_value.status_code = 404
        result = can_access_google_page("https://www.invalid.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
