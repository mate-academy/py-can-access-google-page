import pytest
from unittest import mock
from _pytest.mark import ParameterSet

from app.main import can_access_google_page


class TestAccessGooglePage:
    @pytest.mark.parametrize(
        "url_return_value, connection_return_value",
        [
            pytest.param(
                True,
                False,
                id="only connection false"
            ),
            pytest.param(
                False,
                True,
                id="only url false"
            ),
            pytest.param(
                False,
                False,
                id="connection and url false"
            )
        ]
    )
    def test_access(
        self,
        url_return_value: ParameterSet,
        connection_return_value: ParameterSet
    ) -> None:
        with (
            mock.patch("app.main.valid_google_url") as mocked_url,
            mock.patch("app.main.has_internet_connection") as mocked_connection
        ):
            mocked_url.return_value = url_return_value
            mocked_connection.return_value = connection_return_value

            assert can_access_google_page("google.com") == "Not accessible"
