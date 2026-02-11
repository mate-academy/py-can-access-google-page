from unittest import mock

import app.main as main


class TestCanAccessGoogle:
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page_accessible(
        self, mock_valid_url: mock.Mock, mock_has_internet: mock.Mock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        assert (
            main.can_access_google_page("https://google.com") == "Accessible"
        )

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible_when_no_internet(
        self, mock_valid_url: mock.Mock, mock_has_internet: mock.Mock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        assert (
            main.can_access_google_page("https://google.com")
            == "Not accessible"
        )

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible_when_invalid_url(
        self, mock_valid_url: mock.Mock, mock_has_internet: mock.Mock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        assert (
            main.can_access_google_page("https://google.com")
            == "Not accessible"
        )

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible_when_invalid_url_and_no_internet(
        self, mock_valid_url: mock.Mock, mock_has_internet: mock.Mock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = False
        assert (
            main.can_access_google_page("https://google.com")
            == "Not accessible"
        )
