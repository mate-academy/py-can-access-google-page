from unittest import mock, TestCase

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
class TestApp(TestCase):
    def test_have_access(self, mock_response: bool,
                         mock_current_time: bool) -> None:
        mock_response.return_value = True
        mock_current_time.return_value = True
        assert can_access_google_page("google.com") == "Accessible"

    def test_dont_have_access(self, mock_response: bool,
                              mock_current_time: bool) -> None:
        mock_response.return_value = False
        mock_current_time.return_value = False
        assert can_access_google_page("google.com") == "Not accessible"

    def test_dont_have_access_if(self, mock_response: bool,
                                 mock_current_time: bool) -> None:
        mock_response.return_value = True
        mock_current_time.return_value = False
        assert can_access_google_page("google.com") == "Not accessible"

    def test_dont_have_access_if_one(self, mock_response: bool,
                                     mock_current_time: bool) -> None:
        mock_response.return_value = False
        mock_current_time.return_value = True
        assert can_access_google_page("google.com") == "Not accessible"
