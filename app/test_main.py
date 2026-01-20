from app.main import can_access_google_page
import pytest
from unittest import mock


class TestCanAccessGoogleClass:
    @pytest.mark.parametrize(
        "is_valid_url,internet_connection,access_google",
        [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible"),
        ],
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_check_access_page(
        self,
        mock_url_connect: bool,
        mock_connection: bool,
        is_valid_url: bool,
        internet_connection: bool,
        access_google: str,


    ) -> None:
        mock_url_connect.return_value = is_valid_url
        mock_connection.return_value = internet_connection
        assert (
            can_access_google_page(
                "https://www.google.com/"
            )
            == access_google
        )
