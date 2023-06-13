from app.main import can_access_google_page
from unittest import mock
import pytest


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "is_valid,is_connection,expected_result",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_valid_url_and_connection_exists(
            self,
            mocked_valid_google_url: mock.patch,
            mocked_has_internet_connection: mock.patch,
            is_valid: bool,
            is_connection: bool,
            expected_result: str,
    ) -> None:
        mocked_valid_google_url.return_value = is_valid
        mocked_has_internet_connection.return_value = is_connection

        assert (
            can_access_google_page(
                "https://mate.academy/learn?course=all_courses"
            ) == expected_result
        )
