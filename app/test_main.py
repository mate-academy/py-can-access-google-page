from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
class TestAccessGooglePage:
    def test_url_is_invalid_and_has_connection(
            self, mocked_url: mock.MagicMock, mocked_connection: mock.MagicMock
    ) -> None:
        mocked_url.return_value = False
        mocked_connection.return_value = True
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"

    def test_url_is_valid_and_has_no_connection(
            self, mocked_url: mock.MagicMock, mocked_connection: mock.MagicMock
    ) -> None:
        mocked_url.return_value = True
        mocked_connection.return_value = False
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"

    def test_url_is_invalid_and_has_no_connection(
            self, mocked_url: mock.MagicMock, mocked_connection: mock.MagicMock
    ) -> None:
        mocked_url.return_value = False
        mocked_connection.return_value = False
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"

    def test_url_is_valid_and_has_connection(
            self, mocked_url: mock.MagicMock, mocked_connection: mock.MagicMock
    ) -> None:
        mocked_url.return_value = True
        mocked_connection.return_value = True
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Accessible"
