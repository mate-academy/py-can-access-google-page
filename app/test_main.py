from typing import Any
from unittest import TestCase, mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_has_internet_connection: Any,
            mock_valid_google_url: Any
    ) -> None:
        test_cases = [
            {"connection": True, "url": True, "expected": "Accessible"},
            {"connection": False, "url": True, "expected": "Not accessible"},
            {"connection": True, "url": False, "expected": "Not accessible"},
            {"connection": False, "url": False, "expected": "Not accessible"},
        ]

        for test_case in test_cases:
            mock_valid_google_url.return_value = test_case.get("url")
            mock_has_internet_connection.return_value = (
                test_case.get("connection")
            )
            self.assertEqual(
                can_access_google_page("url"),
                test_case.get("expected")
            )
