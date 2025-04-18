from unittest import mock, TestCase
from unittest.mock import MagicMock
from app.main import can_access_google_page


class TestThirdFunction(TestCase):
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_access_google_page_should_return_accessible(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock
    ) -> None:
        assert can_access_google_page("Hello") == "Accessible"
        mock_valid_google_url.assert_called_once()
        mock_has_internet_connection.assert_called_once()
