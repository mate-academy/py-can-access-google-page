import pytest
from unittest import mock
from app.main import can_access_google_page


class Test:
    @pytest.mark.parametrize(
        "response, current_time, result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_google_url,
                                    mock_internet_connection,
                                    response,
                                    current_time,
                                    result
                                    ):
        mock_google_url.return_value = response
        mock_internet_connection.return_value = current_time
        assert can_access_google_page("google.com") == result
