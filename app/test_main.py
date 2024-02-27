import unittest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_valid_url_and_connection_exists(
            self,
            mocked_valid_google_url: mock.Mock,
            mocked_has_internet_connection: mock.Mock
    ) -> None:
        mocked_valid_google_url.return_value = True
        mocked_has_internet_connection.return_value = True
        assert can_access_google_page("valid_url") == "Accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_valid_url_is_invalid(
            self,
            mocked_valid_google_url: mock.Mock,
            mocked_has_internet_connection: mock.Mock
    ) -> None:
        mocked_valid_google_url.return_value = False
        mocked_has_internet_connection.return_value = True
        assert can_access_google_page("valid_url") == "Not accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_no_internet_connection(
            self,
            mocked_valid_google_url: mock.Mock,
            mocked_has_internet_connection: mock.Mock
    ) -> None:
        mocked_valid_google_url.return_value = True
        mocked_has_internet_connection.return_value = False
        assert can_access_google_page("valid_url") == "Not accessible"
