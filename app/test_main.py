import pytest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "url_return,connection_return,result",
        [
            pytest.param(
                False,
                True,
                "Not accessible",
                id="invalid google url"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="time less then 6"
            ),
            pytest.param(
                True,
                True,
                "Accessible",
                id="is all right"
            )
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mocked_connection,
            mocked_url,
            url_return,
            connection_return,
            result
    ):
        mocked_connection.return_value = connection_return
        mocked_url.return_value = url_return
        assert can_access_google_page('google') == result
