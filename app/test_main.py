import datetime
import unittest
from unittest.mock import patch, MagicMock

from app.main import \
    valid_google_url, has_internet_connection, can_access_google_page


class TestCanAccessGoogle(unittest.TestCase):

    @patch("app.main.requests")
    def test_valid_google_url_True(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.get.return_value = mock_response
        assert valid_google_url(self) is True

    @patch("app.main.requests")
    def test_valid_google_url_False(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_request.get.return_value = mock_response
        assert valid_google_url(self) is False

    @patch("app.main.datetime")
    def test_has_internet_connection_False(self, mock_date):
        mock_date.datetime.now.return_value =\
            datetime.datetime(2022, 3, 14, 5, 45, 45, 1)
        assert has_internet_connection() is False

    @patch("app.main.datetime")
    def test_has_internet_connection_True(self, mock_date):
        mock_date.datetime.now.return_value = \
            datetime.datetime(2022, 3, 14, 9, 45, 45, 1)
        assert has_internet_connection() is True

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_2_False(
            self, mock_valid_url, mock_internet_connection):
        mock_internet_connection.return_value = False
        mock_valid_url.return_value = True
        assert \
            can_access_google_page("https://www.google.com/") == \
            "Not accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_2_True(
            self, mock_valid_url, mock_internet_connection):
        mock_internet_connection.return_value = True
        mock_valid_url.return_value = True
        assert \
            can_access_google_page("https://www.google.com/") == \
            "Accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_1_True_1_False(
            self, mock_valid_url, mock_internet_connection):
        mock_internet_connection.return_value = False
        mock_valid_url.return_value = True
        assert \
            can_access_google_page("https://www.google.com/") == \
            "Not accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_1_True_1_False(
            self, mock_valid_url, mock_internet_connection):
        mock_internet_connection.return_value = True
        mock_valid_url.return_value = False
        assert \
            can_access_google_page("https://www.google.com/") == \
            "Not accessible"
