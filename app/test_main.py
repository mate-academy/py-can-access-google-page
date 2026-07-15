import pytest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccess:
    @pytest.mark.parametrize(
        "is_url_valid,has_connection,expected",
        [
            pytest.param(True, True, "Accessible"),
            pytest.param(False, False, "Not accessible"),
            pytest.param(True, False, "Not accessible"),
            pytest.param(False, True, "Not accessible"),
        ],
        ids=[
            "both conditions are met",
            "both conditions are not met",
            "no internet connection",
            "url is not valid",
        ],
    )
    def test_can_access_google_page(
        self, is_url_valid: bool, has_connection: bool, expected: str
    ) -> None:
        with (
            mock.patch("app.main.valid_google_url") as mocked_validation,
            mock.patch("app.main.has_internet_connection") as mocked_connect,
        ):
            mocked_validation.return_value = is_url_valid
            mocked_connect.return_value = has_connection

            assert can_access_google_page("google.com") == expected
