from unittest import mock

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url, has_internet_connection, access_page",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible")
        ],
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_check_can_access_google_page(
            self,
            mocked_url_valid: callable,
            mocked_connection: callable,
            valid_url: bool,
            has_internet_connection: bool,
            access_page: str
    ) -> None:
        mocked_url_valid.return_value = valid_url
        mocked_connection.return_value = has_internet_connection
        assert can_access_google_page(
            "https: // www.google.com /"
        ) == access_page
