import unittest
from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
class TestCanAccessGooglePage(unittest.TestCase):
    def test_has_internet_and_valid_url(self,
                                        valid_google_url: MagicMock,
                                        has_internet_connection: MagicMock
                                        ) -> None:
        valid_google_url.return_value = True
        has_internet_connection.return_value = True
        assert can_access_google_page("") == "Accessible"

    def test_no_internet_and_valid_url(self,
                                       valid_google_url: MagicMock,
                                       has_internet_connection: MagicMock
                                       ) -> None:
        valid_google_url.return_value = True
        has_internet_connection.return_value = False
        assert can_access_google_page("") == "Not accessible"

    def test_has_internet_and_not_valid_url(self,
                                            valid_google_url: MagicMock,
                                            has_internet_connection: MagicMock
                                            ) -> None:
        valid_google_url.return_value = False
        has_internet_connection.return_value = True
        assert can_access_google_page("") == "Not accessible"
