from unittest import mock

import pytest

from app.main import can_access_google_page


def test_valid_google_url_exists() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        can_access_google_page("https://mate.academy")
        mocked_url.assert_called_once()


def test_has_internet_connection_exists() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        can_access_google_page("https://mate.academy")
        mocked_connection.assert_called_once()


@pytest.mark.parametrize(
    "url_status, connection_status, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
    url_status: bool,
    connection_status: bool,
    result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=url_status),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=connection_status
        )
    ):
        assert can_access_google_page("https://mate.academy") == result
