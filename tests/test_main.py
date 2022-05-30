from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
class TestCanAccessGooglePage:

    def test_can_access_if_has_internet_connection_and_valid_url(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ):

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        assert can_access_google_page("www.qwerty.com") == "Accessible"

    def test_cant_access_if_has_not_internet_connection(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ):

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        assert can_access_google_page("www.qwerty.com") == "Not accessible"

    def test_cant_access_if_url_is_not_valid(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ):

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        assert can_access_google_page("www.qwerty.com") == "Not accessible"

    def test_cant_access_if_url_is_not_valid_and_has_not_internet_connection(
            self,
            mock_valid_google_url,
            mock_has_internet_connection
    ):

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False

        assert can_access_google_page("www.qwerty.com") == "Not accessible"
