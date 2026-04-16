from app.main import can_access_google_page
from unittest.mock import patch
import unittest
from unittest.mock import MagicMock


class TestGoogleAccess(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_access_logic(
            self,
            mock_inet: MagicMock,
            mock_valid: MagicMock
    ) -> None:
        cases = [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ]
        for is_valid, internet_up, expected in cases:
            with self.subTest(is_valid=is_valid, internet=internet_up):
                mock_valid.return_value = is_valid
                mock_inet.return_value = internet_up
                self.assertEqual(can_access_google_page("any-url"), expected)
