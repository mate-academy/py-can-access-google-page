import unittest

from unittest.mock import MagicMock
from unittest.mock import patch

from app import main


class TestMain(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_has_internet_connection: MagicMock,
            mock_valid_google_url: MagicMock
    ) -> None:
        test_cases = [
            {
                "url": "https://www.google.com",
                "internet": True,
                "valid_url": True,
                "expected": "Accessible"
            },
            {
                "url": "https://www.notgoogle.com",
                "internet": True,
                "valid_url": False,
                "expected": "Not accessible"
            },
            {
                "url": "https://www.google.com",
                "internet": False,
                "valid_url": True,
                "expected": "Not accessible"
            },
            {
                "url": "https://www.notgoogle.com",
                "internet": False,
                "valid_url": False,
                "expected": "Not accessible"
            },
        ]

        for test in test_cases:
            with self.subTest(test=test):
                mock_has_internet_connection.return_value = test["internet"]
                mock_valid_google_url.return_value = test["valid_url"]
                result = main.can_access_google_page(test["url"])
                self.assertEqual(result, test["expected"])


if __name__ == "__main__":
    unittest.main()
