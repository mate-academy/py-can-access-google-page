import unittest
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
class TestCanAccessGooglePage(unittest.TestCase):

    def test_can_access_with_correct_url_and_time(self,
                                                  internet_connection: bool,
                                                  valid_url: bool) -> None:
        assert can_access_google_page(valid_url) == "Accessible"

    def test_cannot_access_with_incorrect_time(self,
                                               internet_connection: bool,
                                               valid_url: bool) -> None:
        internet_connection.return_value = False
        assert can_access_google_page(valid_url) == "Not accessible"

    def test_cannot_access_with_incorrect_url(self,
                                              internet_connection: bool,
                                              valid_url: bool) -> None:
        valid_url.return_value = False
        assert can_access_google_page(valid_url) == "Not accessible"
