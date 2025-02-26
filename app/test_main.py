import unittest
from unittest import mock
from app.main import can_access_google_page


class GoogleTest(unittest.TestCase):
    def test_can_access_google_page_two_true(self):
        with mock.patch("app.main.has_internet_connection", return_value=True), \
             mock.patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("test_site")
            self.assertEqual(result, "Accessible")

    def test_can_access_google_page_two_false(self):
        with mock.patch("app.main.has_internet_connection", return_value=False), \
             mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("test_site")
            self.assertEqual(result, "Not accessible")

    def test_can_access_google_page_true_false(self):
        with mock.patch("app.main.has_internet_connection", return_value=True), \
             mock.patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page("test_site")
            self.assertEqual(result, "Not accessible")

    def test_can_access_google_page_false_true(self):
        with mock.patch("app.main.has_internet_connection", return_value=False), \
                mock.patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page("test_site")
            self.assertEqual(result, "Not accessible")
