import pytest

from unittest import mock

from unittest.mock import MagicMock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
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
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
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

        mocked_has_internet_connection.assert_called_once()
        if connection_status:
            mocked_valid_google_url.assert_called_once()
        else:
            mocked_valid_google_url.assert_not_called()
