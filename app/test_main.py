import pytest

from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "has_internet_connection, valid_google_url, expected",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="has internet connection and valid google url",
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="has no internet connection and valid google url",
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="has internet connection and invalid google url",
            ),
            pytest.param(
                False,
                False,
                "Not accessible",
                id="has no internet connection and invalid google url",
            )
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
        self,
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected: str
    ) -> None:
        mock_has_internet_connection.return_value = has_internet_connection
        mock_valid_google_url.return_value = valid_google_url
        assert can_access_google_page("https://www.google.com") == expected
