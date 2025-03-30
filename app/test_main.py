import pytest
import datetime

from unittest import mock

from app.main import can_access_google_page, has_internet_connection


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        pytest.param(
            False, False, "Not accessible",
            id="No connection and wrong URL"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="There is a connection, but the url is not valid"),
        pytest.param(
            True, False, "Not accessible",
            id="There is no connection, but the url is correct"),
        pytest.param(
            True, True, "Accessible",
            id="Accessible"),
    ]
)
def test_should_return_correct_values(
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_google_url,
        mock.patch("app.main.has_internet_connection") as mock_has_internet
    ):
        mock_google_url.return_value = valid_url
        mock_has_internet.return_value = has_internet
        assert can_access_google_page("google.com") == result


def test_has_internet_connection() -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value = datetime.datetime(
            2024, 8, 8, 10, 0, 0
        )
        assert has_internet_connection() is True

        mock_datetime.datetime.now.return_value = datetime.datetime(
            2024, 8, 8, 2, 0, 0
        )
        assert has_internet_connection() is False
