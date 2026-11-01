import pytest
from unittest import mock
from typing import Generator

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "has_internet_connection,valid_google_url,expected",
        [
            pytest.param(
                True, True, "Accessible",
                id="should return 'Accessible'"
            ),
            pytest.param(
                False, True, "Not accessible",
                id="should return 'Not accessible' when "
                   "has not internet connection"
            ),
            pytest.param(
                True, False, "Not accessible",
                id="should return 'Not accessible' when google url is invalid"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="should return 'Not accessible' when both "
                   "has not internet connection and "
                   "google url are invalid"
            ),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google(
        self,
        mock_has_internet_connection: Generator[mock.MagicMock, None, None],
        mock_valid_google_url: Generator[mock.MagicMock, None, None],
        has_internet_connection: bool,
        valid_google_url: bool,
        expected: str
    ) -> None:
        mock_has_internet_connection.return_value = has_internet_connection
        mock_valid_google_url.return_value = valid_google_url

        result = can_access_google_page("https://google.com")

        assert result == expected
