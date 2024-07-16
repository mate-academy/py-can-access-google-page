import pytest

from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "internet, valid_url, expected",
        [
            pytest.param(
                True, True,
                "Accessible",
                id="Should be accessible"
            ),
            pytest.param(
                True, False,
                "Not accessible",
                id="Should not be accessible"
            ),
            pytest.param(
                False, True,
                "Not accessible",
                id="Should not be accessible"
            ),
            pytest.param(
                False, False,
                "Not accessible",
                id="Should not be accessible"
            )
        ]

    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_valid_google_url: None,
            mock_has_internet_connection: None,
            internet: bool,
            valid_url: bool,
            expected: str) -> None:
        mock_valid_google_url.return_value = internet
        mock_has_internet_connection.return_value = valid_url
        result = can_access_google_page("http://www.google.com")
        assert result == expected

# write your code here
