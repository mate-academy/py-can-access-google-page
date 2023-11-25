from unittest import mock
import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @pytest.mark.parametrize(
        "internet_connection, is_valid_url, url, result",
        [
            pytest.param(
                True,
                True,
                "https://www.google.com",
                "Accessible",
                id="can access google page with valid url and connection"
            ),
            pytest.param(
                False,
                True,
                "https://www.invalidurl.com",
                "Not accessible",
                id="can access google page with invalid url"
            ),
            pytest.param(
                True,
                False,
                "https://www.google.com",
                "Not accessible",
                id="can access google page without connection"
            )
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_has_internet_connection: mock.MagicMock,
            mock_valid_google_url: mock.MagicMock,
            internet_connection: bool,
            is_valid_url: bool,
            url: str,
            result: str
    ) -> None:
        mock_valid_google_url.return_value = is_valid_url
        mock_has_internet_connection.return_value = internet_connection
        assert can_access_google_page(url) == result
