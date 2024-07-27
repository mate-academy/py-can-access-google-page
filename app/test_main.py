from unittest import mock
import pytest
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "is_valid_url, has_connection, expected_result",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_valid_url: mock.Mock,
                                    mock_has_connection: mock.Mock,
                                    is_valid_url: bool,
                                    has_connection: bool,
                                    expected_result: str) -> None:
        mock_valid_url.return_value = is_valid_url
        mock_has_connection.return_value = has_connection

        result = can_access_google_page("https://www.google.com")

        assert result == expected_result
