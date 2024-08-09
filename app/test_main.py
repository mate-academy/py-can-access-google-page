from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_access() -> tuple:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection") as mock_connection
    ):
        yield mock_valid_google_url, mock_connection


@pytest.mark.parametrize(
    "valid_url, has_internet, result, description",
    [
        (
            True,
            True,
            "Accessible",
            "Valid url and internet connection should return 'Accessible'"
        ),
        (
            False,
            False,
            "Not accessible",
            "Invalid url and internet connection "
            "should return 'Not accessible'"
        ),
        (
            True,
            False,
            "Not accessible",
            "Valid url but no internet connection "
            "should return 'Not accessible'"
        ),
        (
            False,
            True,
            "Not accessible",
            "Invalid url and working internet connection "
            "should return 'Not accessible'"
        ),
    ]
)
def test_can_access_google_page(
        mock_access: tuple,
        valid_url: bool,
        has_internet: bool,
        result: str,
        description: str
) -> None:
    mock_valid_google_url, mock_internet_connection = mock_access
    mock_valid_google_url.return_value = valid_url
    mock_internet_connection.return_value = has_internet

    assert can_access_google_page("example.com") == result, description
