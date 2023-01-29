from app.main import can_access_google_page
from unittest import mock
import pytest


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url,net_connection,accessibility",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="should access page if both"
                   "'valid url' and 'connection' are True"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="should not access page if only 'valid url' is Truer"
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="should not access page if only 'connection' is True"
            ),
            pytest.param(
                False,
                False,
                "Not accessible",
                id="should not access page if both"
                   "'valid url' and 'connection' are True"
            ),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_get_access_correctly(
            self,
            mocked_url: bool,
            mocked_connection: bool,
            valid_url: bool,
            net_connection: bool,
            accessibility: str
    ) -> str:
        mocked_url.return_value = valid_url
        mocked_connection.return_value = net_connection
        assert can_access_google_page("https://www.google.com/")\
               == accessibility
