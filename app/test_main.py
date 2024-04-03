import unittest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("requests.get")
    @mock.patch("datetime.datetime")
    def test_can_access_google_page(self,
                                    mock_time: mock.MagicMock,
                                    mock_get: mock.MagicMock) -> None:
        # Response check from valid_google_url function
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Time check from has_internet_connection
        mock_now = mock.MagicMock()
        mock_now.hour = 21
        mock_time.now.return_value = mock_now

        main_func_call = can_access_google_page("https://somefakegoogle.net")

        mock_get.assert_called_once_with("https://somefakegoogle.net")
        mock_time.now.assert_called_once()

        self.assertEqual(main_func_call, "Accessible")
