from unittest.mock import patch
from app.main import can_access_google_page
import pytest


class TestAccessGooglePage:
    @pytest.mark.parametrize(
        "param_one, param_two, result",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_valid_url_and_connection_exists(
            self,
            mock_valid: bool,
            mock_connection: bool,
            param_one: bool,
            param_two: bool,
            result: str
    ) -> None:
        mock_valid.return_value = param_one
        mock_connection.return_value = param_two
        assert can_access_google_page("www.google.com") == result
