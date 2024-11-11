import unittest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @mock.patch("valid_google_url.has_internet_connection")
    def test_accessible(self, mock_valid_google_url: str,
                        mock_has_internet_connection: bool
                        ) -> None:
        result = can_access_google_page("")
        self.assertEquals(result, "Accessible")

    @mock.patch("valid_google_url.has_internet_connection")
    def test_not_accessible_not_url(self, mock_valid_google_url: str,
                                    mock_has_internet_connection: bool
                                    ) -> None:
        result = can_access_google_page("")
        self.assertEquals(result, "Not accessible")

    @mock.patch("valid_google_url.has_internet_connection")
    def test_not_accessible_not_internet(self, mock_valid_google_url: str,
                                         mock_has_internet_connection: bool
                                         ) -> None:
        result = can_access_google_page("")
        self.assertEquals(result, "Not accessible")
