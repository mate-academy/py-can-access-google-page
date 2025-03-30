import pytest
from unittest import mock
from app.main import can_access_google_page


class TestGooglePageAccess:
    @pytest.mark.parametrize(
        "internet_connection,valid_url,expected_massage",
        [
            pytest.param(
                True, True, "Accessible",
                id="internet_connection: True, valid_url: True"
            ),
            pytest.param(
                True, False, "Not accessible",
                id="internet_connection: True, valid_url: False"
            ),
            pytest.param(
                False, True, "Not accessible",
                id="internet_connection: False, valid_url: True"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="internet_connection: False, valid_url: False"
            )
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
            self,
            mocked_internet_connection: mock.MagicMock,
            mocked_url: mock.MagicMock,
            internet_connection: bool,
            valid_url: bool,
            expected_massage: str
    ) -> None:
        mocked_internet_connection.return_value = internet_connection
        mocked_url.return_value = valid_url
        assert can_access_google_page("google.com") == expected_massage
