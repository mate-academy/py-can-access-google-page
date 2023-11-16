from unittest import mock
import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "has_internet, is_valid, expected_result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(
        self,
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        has_internet: bool,
        is_valid: bool,
        expected_result: str
    ) -> None:
        mocked_valid_google_url.return_value = is_valid
        mocked_has_internet_connection.return_value = has_internet
        result = can_access_google_page("http://google.com")
        assert result == expected_result
