import pytest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_url, valid_internet_conn, expected",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="URL verification was successful"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="not internet connection"
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="url isn't valid"
            )
        ]
    )
    def test_access_google_page(
            self,
            valid_url: bool,
            valid_internet_conn: bool,
            expected: bool,
    ) -> None:
        with (mock.patch("app.main.valid_google_url") as mocked_url,
              mock.patch("app.main.has_internet_connection")
              as mocked_connection):
            mocked_url.return_value = valid_url
            mocked_connection.return_value = valid_internet_conn
            assert can_access_google_page("https://www.google.com/") \
                   == expected
