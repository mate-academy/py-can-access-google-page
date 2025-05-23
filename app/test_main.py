from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_returns_accessible_when_internet_and_url_valid(
        self, mock_has_internet: mock.Mock, mock_valid_url: mock.Mock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        result = can_access_google_page("https://google.com")
        assert result == "Accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_returns_not_accessible_when_no_internet(
        self, mock_has_internet: mock.Mock, mock_valid_url: mock.Mock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_returns_not_accessible_when_url_invalid(
        self, mock_has_internet: mock.Mock, mock_valid_url: mock.Mock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_returns_not_accessible_when_both_conditions_false(
        self, mock_has_internet: mock.Mock, mock_valid_url: mock.Mock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = False

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
