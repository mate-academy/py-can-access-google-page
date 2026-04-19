import unittest
from unittest.mock import patch, MagicMock


from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_accessible(
        self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://google.com"), "Accessible"
        )

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_no_internet(
        self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://google.com"), "Not accessible"
        )

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_invalid_url(
        self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://notgoogle.com"), "Not accessible"
        )

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_no_internet_and_invalid_url(
        self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://notgoogle.com"), "Not accessible"
        )


if __name__ == "__main__":
    unittest.main()
