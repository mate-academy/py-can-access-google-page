import pytest

from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "valid_google_url_value, "
        "has_internet_connection_value, "
        "expected_result",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible"),
        ],
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_internet_connection: mock.Mock,
                                    mock_valid_google_url: mock.Mock,
                                    valid_google_url_value: bool,
                                    has_internet_connection_value: bool,
                                    expected_result: str) -> None:
        test_url = "https://www.google.com"
        mock_valid_google_url.return_value = valid_google_url_value
        mock_internet_connection.return_value = has_internet_connection_value
        assert can_access_google_page(test_url) == expected_result
        mock_internet_connection.assert_called_once()
        if has_internet_connection_value:
            mock_valid_google_url.assert_called_once_with(test_url)
