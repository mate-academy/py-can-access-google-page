import pytest

from unittest import mock
from app.main import can_access_google_page
from typing import Any


valid_url = "https://www.google.com/"
invalid_url = "https://invalid_url"


@pytest.mark.parametrize(
    "has_internet_connection, has_valid_google_url, url, expected",
    [
        pytest.param(
            True,
            True,
            valid_url,
            "Accessible",
            id="accessible when URL is valid and has internet connection"
        ),
        pytest.param(
            True,
            False,
            invalid_url,
            "Not accessible",
            id="not accessible when URL is invalid and has internet connection"
        ),
        pytest.param(
            False,
            True,
            valid_url,
            "Not accessible",
            id="not accessible when has no internet connection"
        ),
        pytest.param(
            False,
            False,
            valid_url,
            "Not accessible",
            id="not accessible when URL is invalid and no internet connection"
        ),

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_connection: Any,
                                mock_google_url: Any,
                                has_internet_connection: bool,
                                has_valid_google_url: bool,
                                url: str,
                                expected: str) -> None:
    mock_internet_connection.return_value = has_internet_connection
    mock_google_url.return_value = has_valid_google_url
    assert can_access_google_page(url) == expected
