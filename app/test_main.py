from unittest import mock
import pytest
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url, has_internet, access_page",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible")
        ],
        ids=[
            "Valid URL, Has Internet",
            "Valid URL, No Internet",
            "Invalid URL, Has Internet",
            "Invalid URL, No Internet"
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mocked_url_valid: callable,
            mocked_connection: callable,
            valid_url: bool,
            has_internet: bool,
            access_page: str
    ) -> None:
        mocked_url_valid.return_value = valid_url
        mocked_connection.return_value = has_internet
        assert can_access_google_page("https://www.google.com/") == access_page
