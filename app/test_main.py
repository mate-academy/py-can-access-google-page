import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    @pytest.mark.parametrize(
        "connection_status, url_validation, expected_result",
        [
            (True, True, "Accessible"),
            (False, False, "Not accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible")
        ],
        ids=[
            "Connected",
            "Not valid url and no internet connection",
            "No connection",
            "Not valid url"
        ]
    )
    def test_can_access_google_page(
            self,
            mocked_valid_google_url: MagicMock,
            mocked_has_internet_connection: MagicMock,
            connection_status: bool,
            url_validation: bool,
            expected_result: str
    ) -> None:
        mocked_valid_google_url.return_value = url_validation
        mocked_has_internet_connection.return_value = connection_status
        assert (can_access_google_page("https://www.google.com")
                == expected_result)
