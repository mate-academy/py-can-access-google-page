from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "mocked_url, mocked_connection, expected",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
        ],
        ids=[
            "Valid url and available internet connection",
            "Invalid url but available internet connection",
            "Valid url but no internet connection",
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_valid_url: MagicMock,
            mock_internet_connection: MagicMock,
            mocked_url: str,
            mocked_connection: str,
            expected: str
    ) -> None:
        mock_valid_url.return_value = mocked_url
        mock_internet_connection.return_value = mocked_connection

        assert can_access_google_page("https://www.google.com") == expected
