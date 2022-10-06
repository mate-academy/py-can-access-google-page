import pytest
from app.main import can_access_google_page
from unittest import mock
from typing import Callable


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "valid_google_url, internet_connection, expected",
    [
        (
            True,
            True,
            "Accessible",
        ),
        (
            False,
            False,
            "Not accessible",
        ),
        (
            False,
            True,
            "Not accessible",
        ),
        (
            True,
            False,
            "Not accessible",
        ),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: Callable,
        mock_has_internet_connection: Callable,
        valid_google_url: bool,
        internet_connection: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page("www.google.com") == expected
