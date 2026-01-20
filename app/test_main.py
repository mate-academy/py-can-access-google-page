from app.main import can_access_google_page

from unittest import mock

import pytest


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "is_valid_url, has_internet_connection, access_google",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible")
        ],
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_check_can_access(
            self,
            mocked_url_connection: callable,
            mocked_connection: callable,
            is_valid_url: bool,
            has_internet_connection: bool,
            access_google: str
    ) -> None:
        mocked_url_connection.return_value = is_valid_url
        mocked_connection.return_value = has_internet_connection
        assert can_access_google_page(
            "https: // www.google.com / search?q = ukraine"
        ) == access_google
