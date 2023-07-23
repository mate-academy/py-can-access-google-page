from unittest import mock
import pytest

from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection, \
         mock.patch("app.main.valid_google_url") as mocked_url:

        can_access_google_page("https://google.com.ua")
        mocked_url.assert_called_once_with(
            "https://google.com.ua"
        )
        mocked_connection.assert_called_once()

        @pytest.mark.parametrize(
            "mocked_connection, mocked_url, outcome",
            [
                (True, True, "Accessible"),
                (False, True, "Not accessible"),
                (True, False, "Not accessible"),
                (False, False, "Not accessible")
            ]
        )
        def test_if_one_can_access_google_page(
                mocked_connection: bool,
                mocked_url: bool,
                outcome: str
        ) -> None:
            assert can_access_google_page("https://google.com.ua") == outcome
