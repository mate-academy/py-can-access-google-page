from unittest import mock

import pytest

from app.main import can_access_google_page


class TestAccessGooglePage:
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    @pytest.mark.parametrize(
        "time_connection, response_request, expected_result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible")
        ]
    )
    def test_access_google_page(self,
                                mock_current_time,
                                mock_response,
                                time_connection,
                                response_request,
                                expected_result):
        mock_current_time.return_value = time_connection
        mock_response.return_value = response_request
        assert can_access_google_page("") == expected_result
