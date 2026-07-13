import unittest


from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_when_url_valid_and_has_internet(self,
                                                        mock_url: MagicMock,
                                                        mock_internet:
                                                        MagicMock
                                                        ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = True

        result = can_access_google_page("https://google.com")

        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_cannot_access_if_only_valid_url(self,
                                             mock_url: MagicMock,
                                             mock_internet: MagicMock
                                             ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://google.com")

        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_cannot_access_if_invalid_url(self,
                                          mock_url: MagicMock,
                                          mock_internet: MagicMock
                                          ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("https://bad.com")

        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_cannot_access_if_invalid_url_and_no_internet(self,
                                                          mock_url: MagicMock,
                                                          mock_internet:
                                                          MagicMock
                                                          ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = False

        result = can_access_google_page("https://bad.com")

        self.assertEqual(result, "Not accessible")
