from unittest import mock

from app.main import can_access_google_page


class TestMain():
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page_with_valid_url_and_time(
            self,
            mock_has_internet_connection: mock.MagicMock,
            mock_valid_google_url: mock.MagicMock
    ) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        assert can_access_google_page("mock") == "Accessible"
        mock_has_internet_connection.assert_called_once()
        mock_valid_google_url.assert_called_once()

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_return_not_accessible_when_no_internet_connection(
            self,
            mock_has_internet_connection: mock.MagicMock,
            mock_valid_google_url: mock.MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        assert can_access_google_page("mock") == "Not accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_return_not_accessible_when_non_valid_url(
            self,
            mock_has_internet_connection: mock.MagicMock,
            mock_valid_google_url: mock.MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        assert can_access_google_page("mock") == "Not accessible"
