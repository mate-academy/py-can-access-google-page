from unittest import mock, TestCase
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page_correct(self,
                                            mock_has_internet:
                                            mock.MagicMock,
                                            mock_valid_url:
                                            mock.MagicMock
                                            ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        result = can_access_google_page("https://www.google.com")

        assert result == "Accessible"
        mock_has_internet.assert_called_once()
        mock_valid_url.assert_called_once_with("https://www.google.com")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page_no_connect(self,
                                               mock_has_internet:
                                               mock.MagicMock,
                                               mock_valid_url:
                                               mock.MagicMock
                                               ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
        mock_has_internet.assert_called_once()
        mock_valid_url.assert_not_called()

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page_wrong_url(self,
                                              mock_has_internet:
                                              mock.MagicMock,
                                              mock_valid_url:
                                              mock.MagicMock
                                              ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False

        result = can_access_google_page("https://wrong.com")

        assert result == "Not accessible"
        mock_has_internet.assert_called_once()
        mock_valid_url.assert_called_once_with("https://wrong.com")
