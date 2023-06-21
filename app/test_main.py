from unittest import mock

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "mock_has_internet_connection_result,"
        "mock_valid_google_url_result,"
        "can_access_google_page_result",
        [
            pytest.param(True, True, "Accessible",
                         id="is accessible with (has_internet_connection, "
                            "valid_google_url) = (true, true)"),
            pytest.param(True, False, "Not accessible",
                         id="not accessible with (has_internet_connection, "
                            "valid_google_url) = (true, false)"),
            pytest.param(False, True, "Not accessible",
                         id="not accessible with (has_internet_connection, "
                            "valid_google_url) = (false, true)"),
            pytest.param(False, False, "Not accessible",
                         id="not accessible with (has_internet_connection, "
                            "valid_google_url) = (false, false)")
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
            self,
            mock_valid_google_url: mock.MagicMock,
            mock_has_internet_connection: mock.MagicMock,
            mock_has_internet_connection_result: bool,
            mock_valid_google_url_result: bool,
            can_access_google_page_result: str
    ) -> None:
        print(type(mock_valid_google_url))
        mock_valid_google_url.return_value = (
            mock_has_internet_connection_result
        )
        mock_has_internet_connection.return_value = (
            mock_valid_google_url_result
        )
        assert can_access_google_page("url") == can_access_google_page_result
