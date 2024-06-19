import unittest
from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
class TestGooglePageAccess(unittest.TestCase):
    def test_can_access_when_connection_and_url_are_true(
            self,
            mocked_url: MagicMock,
            mocked_connection: MagicMock
    ) -> None:
        mocked_connection.return_value = True
        mocked_url.return_value = True
        assert can_access_google_page("http://google.com") == "Accessible"

    def test__cannot_access_if_only_valid_url(
            self,
            mocked_url: MagicMock,
            mocked_connection: MagicMock
    ) -> None:
        mocked_connection.return_value = False
        mocked_url.return_value = True
        assert can_access_google_page("http://google.com") == "Not accessible"

    def test__cannot_access_if_only_connection(
            self,
            mocked_url: MagicMock,
            mocked_connection: MagicMock
    ) -> None:
        mocked_connection.return_value = True
        mocked_url.return_value = False
        assert can_access_google_page("http://google.com") == "Not accessible"

    def test_cannot_access_when_no_connection_and_no_valid_url(
            self,
            mocked_url: MagicMock,
            mocked_connection: MagicMock
    ) -> None:
        mocked_connection.return_value = False
        mocked_url.return_value = False
        assert can_access_google_page("http://google.com") == "Not accessible"
