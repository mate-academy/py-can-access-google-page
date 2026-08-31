import pytest

from app.main import (valid_google_url,
                      has_internet_connection,
                      can_access_google_page)
from unittest import mock


def test_valid_google_url() -> None:
    with mock.patch("app.main.requests.get") as mock_get:
        mock_get.return_value.status_code = 200

        result = valid_google_url("https://google.com")

        assert result is True

        mock_get.assert_called_once_with("https://google.com")


def test_has_internet_connection() -> None:
    with mock.patch("app.main.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.hour = 10

        result = has_internet_connection()

        assert result is True
        mock_datetime.now.assert_called_once_with()


@pytest.mark.parametrize(
    "google, internet, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Only possible variant to access the google page.",
        ),
        pytest.param(False, True, "Not accessible", id="Google not valid"),
        pytest.param(True, False, "Not accessible",
                     id="No internet connection"),
        pytest.param(False, False, "Not accessible", id="Everything is bad("),
    ],
)
def test_can_access_google_page(
        google: bool, internet: bool, result: str) -> None:
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        with mock.patch("app.main.valid_google_url") as mock_google:
            mock_internet.return_value = internet
            mock_google.return_value = google

            actual_result = can_access_google_page("https://google.com")

            assert actual_result == result
