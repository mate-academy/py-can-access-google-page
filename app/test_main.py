from unittest import mock
import pytest
from app.main import can_access_google_page


class TestGooglePageAccess:
    @pytest.mark.parametrize(
        "internet_connection,valid_url,message",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="internet_connection: True, valid_url: True",
            ),
            pytest.param(
                False,
                False,
                "Not accessible",
                id="internet_connection: False, valid_url: False",
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="internet_connection: True, valid_url: False",
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="internet_connection: False, valid_url: True",
            )
        ]
    )
    def test_can_access_google_page(
            self,
            internet_connection: bool,
            valid_url: bool,
            message: str,
    ) -> None:
        with (mock.patch("app.main.has_internet_connection") as
              mocked_internet_connection,
              mock.patch("app.main.valid_google_url") as
              mocked_valid_url):
            mocked_internet_connection.return_value = internet_connection
            mocked_valid_url.return_value = valid_url
            assert can_access_google_page("url") == message
