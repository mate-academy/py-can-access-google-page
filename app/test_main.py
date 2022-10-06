from typing import Callable

from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="Should return Accessible"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Should return Not accessible if at least one False"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Should return Not accessible if at least one False"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Should return Not accessible if at least one False"
        )
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: Callable,
        mock_has_internet_connection: Callable,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("https://www.google.com.ua/") == expected
