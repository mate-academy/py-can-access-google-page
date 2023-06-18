import pytest
from unittest import mock

from app.main import can_access_google_page


class TestAccessPage:
    @pytest.mark.parametrize(
        "valid_url, has_internet, res_page",
        [
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
            (True, True, "Accessible")
        ],
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mocked_url_valid: mock.Mock,
            mocked_connection: mock.Mock,
            valid_url: bool,
            has_internet: bool,
            res_page: str) -> None:
        mocked_url_valid.return_value = valid_url
        mocked_connection.return_value = has_internet
        assert can_access_google_page("https://www.google.com/") == res_page
