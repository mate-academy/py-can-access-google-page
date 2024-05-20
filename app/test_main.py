import unittest
from unittest.mock import patch
import sys
import os
from app.main import can_access_google_page
from typing import Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_when_both_conditions_true(self, mock_has_internet_connection: Any, mock_valid_google_url: Any) -> None:  # noqa: E501
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        self.assertEqual(can_access_google_page("http://www.google.com"), "Accessible")  # noqa: E501

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_when_no_internet_connection(self, mock_has_internet_connection: Any, mock_valid_google_url: Any) -> None:  # noqa: E501
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        self.assertEqual(can_access_google_page("http://www.google.com"), "Not accessible")  # noqa: E501

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_when_invalid_google_url(self, mock_has_internet_connection: Any, mock_valid_google_url: Any) -> None:  # noqa: E501
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        self.assertEqual(can_access_google_page("http://www.google.com"), "Not accessible")  # noqa: E501

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_when_both_conditions_false(self, mock_has_internet_connection: Any, mock_valid_google_url: Any) -> None:  # noqa: E501
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        self.assertEqual(can_access_google_page("http://www.google.com"), "Not accessible")  # noqa: E501


if __name__ == "__main__":
    unittest.main()
