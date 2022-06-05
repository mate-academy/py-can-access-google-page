import pytest

from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "response, current_time, access",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="Should give access"
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="Url isn't valid"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="Current time isn't in range"
            )
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
            self,
            mocked_url_status,
            mocked_time,
            response,
            current_time,
            access,
    ):

        mocked_url_status.return_value = response
        mocked_time.return_value = current_time

        assert can_access_google_page(url=None) == access
        assert mocked_url_status.called_once()
        assert mocked_time.called_once()
