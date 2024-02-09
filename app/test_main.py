from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage():
    @mock.patch("app.main.has_internet_connection", return_value=False)
    @mock.patch("app.main.valid_google_url", return_value=True)
    def test_can_access_google_page_without_connection(
            self,
            mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=True)
    @mock.patch("app.main.valid_google_url", return_value=False)
    def test_can_access_google_page_unavalid_url(
            self,
            mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        url = "https://www.google.com.ua"
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=False)
    @mock.patch("app.main.valid_google_url", return_value=False)
    def test_can_access_google_page_all_false(
            self,
            mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        url = "https://www.google.com.ua"
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=True)
    @mock.patch("app.main.valid_google_url", return_value=True)
    def test_can_access_google_page_all_true(
            self,
            mock_valid_google_url: mock,
            mock_has_internet_connection: mock
    ) -> None:
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Accessible"
