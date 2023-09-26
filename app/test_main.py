from unittest import mock
from app.main import can_access_google_page
import pytest


def test_valid_url_and_connection_exists() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        can_access_google_page("https://google.com")
        mocked_connection.assert_called_once()
        mocked_valid_google_url.assert_called_once()


@pytest.mark.parametrize(
    "return_value_connection, return_value_valid_google_url, expected",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "No connection, valid url",
        "Connection, invalid url",
        "No connection, invalid url",
        "Connection, valid url",
    ]
)
def test_different_cases_for_accesing_google_page(
        return_value_connection: bool,
        return_value_valid_google_url: bool,
        expected: str) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_connection,
        mock.patch("app.main.valid_google_url") as mocked_valid_google_url
    ):
        mocked_connection.return_value = return_value_connection
        mocked_valid_google_url.return_value = return_value_valid_google_url
        assert can_access_google_page("https://google.com") == expected
