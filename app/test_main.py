import pytest
from unittest import mock


from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url, has_connection, result",
        [
            pytest.param(
                True, True, "Accessible"
            ),
            pytest.param(
                True, False, "Not accessible"
            ),
            pytest.param(
                False, True, "Not accessible"
            ),
            pytest.param(
                False, False, "Not accessible"
            )
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mocked_valid_google_url,
            mocked_has_internet_connection,
            valid_url,
            has_connection,
            result
    ):
        mocked_valid_google_url.return_value = valid_url
        mocked_has_internet_connection.return_value = has_connection

        assert can_access_google_page(valid_url) == result
