import pytest
from typing import Callable
from unittest.mock import patch
from app.main import can_access_google_page


class TestAccessGooglePage:
    @pytest.mark.parametrize(
        "has_internet, has_valid, message",
        [
            pytest.param(True,
                         True,
                         "Accessible",
                         id="Should be accessible when "
                            "internet connection and valid url exist"),
            pytest.param(True,
                         False,
                         "Not accessible",
                         id="Should be not accessible when "
                            "internet connection is False"),
            pytest.param(False,
                         True,
                         "Not accessible",
                         id="Should be not accessible when "
                            "valid url is False"),
            pytest.param(False,
                         False,
                         "Not accessible",
                         id="Should be not accessible when "
                            "valid url and internet connection is False")
        ]
    )
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_valid_url_and_connection_exists(
            self,
            mock_has_internet_connection: Callable,
            mock_valid_google_url: Callable,
            has_internet: bool,
            has_valid: bool,
            message: str
    ) -> None:
        mock_has_internet_connection.return_value = has_internet
        mock_valid_google_url.return_value = has_valid
        assert can_access_google_page("www.google.com") == message
