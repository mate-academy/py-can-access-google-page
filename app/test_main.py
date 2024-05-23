from app.main import can_access_google_page, has_internet_connection, valid_google_url
from unittest import mock
import datetime


def test_valid_google_url():
    with mock.patch("requests.get") as mock_response:
        valid_google_url("google.com")
        mock_response.assert_called_once()


def test_internet_connection():
    with mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime.datetime(2024, 5, 22, 10, 0, 0)
        has_internet_connection()
        mock_datetime.assert_called_once()


def test_cannot_access_if_only_valid_url():
    with mock.patch('app.main.has_internet_connection', return_value=False), \
            mock.patch('app.main.valid_google_url', return_value=True):
            assert can_access_google_page('http://www.google.com') == "Not accessible"


def test_cannot_access_if_only_connection():
    with mock.patch('app.main.has_internet_connection', return_value=True), \
            mock.patch('app.main.valid_google_url', return_value=False):
            assert can_access_google_page('http://www.google.com') == "Not accessible"


