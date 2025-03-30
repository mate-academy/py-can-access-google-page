from unittest import mock
import pytest
from app.main import can_access_google_page


class TestGoogleAccess:
    @pytest.mark.parametrize(
        "connection, url, expected_result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible")
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool,
            connection: bool,
            url: bool,
            expected_result: str
    ) -> None:
        mock_has_internet_connection.return_value = connection
        mock_valid_google_url.return_value = url
        assert can_access_google_page("https://google.com") == expected_result
