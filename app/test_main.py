import unittest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_connection: mock.MagicMock,
                                    mock_valid_url: mock.MagicMock) -> None:
        # Mock of has_internet_connection() function
        mock_result_connection = mock.MagicMock()
        mock_connection.return_value = mock_result_connection

        # Mock of valid_google_url() function
        mock_result_valid = mock.MagicMock()
        mock_valid_url.return_value = mock_result_valid

        main_func_call = can_access_google_page("https://somefakegoogle.net")

        mock_valid_url.assert_called_once_with("https://somefakegoogle.net")
        mock_connection.assert_called_once()

        self.assertEqual(main_func_call, "Accessible")
