from unittest.mock import patch, MagicMock
import pytest
from app import main


class TestAccessGooglePage:
    @pytest.mark.parametrize(
        "has_connection,valid_url,expected_result",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ],
        ids=[
            "Connection=True, valid_url=True, Accessible",
            "Connection=True, valid_url=False, Not accessible",
            "Connection=False, valid_url=True, Not accessible",
            "Connection=False, valid_url=False, Not accessible",
        ]
    )
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page(
        self,
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        has_connection: bool,
        valid_url: bool,
        expected_result: str
    ) -> None:
        mock_has_internet_connection.return_value = has_connection
        mock_valid_google_url.return_value = valid_url
        assert (
            main.can_access_google_page("https://google.com")
        ) == expected_result
