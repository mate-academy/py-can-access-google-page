from unittest import TestCase, mock
from app.main import can_access_google_page, has_internet_connection, valid_google_url


class TestConnecting(TestCase):

    def test_can_access_google_page(self) -> None:
        assert (can_access_google_page("http://google.com") == "Accessible"), "Test should return 'Accessible'"

    @mock.patch("app.main.valid_google_url", return_value="http://google.com")
    def test_valid_google_url(self, mock_value) -> None:
        result = valid_google_url(url="http://google.com")
        self.assertEqual(result, True)

    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_has_internet_connection(self, mock_value) -> None:
        result = has_internet_connection()
        self.assertEqual(result, True)
