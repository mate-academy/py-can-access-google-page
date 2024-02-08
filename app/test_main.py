import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "valid_url, has_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mocked_url: Callable,
        mock_connection: Callable,
        valid_url: bool,
        has_connection: bool,
        result: str
) -> None:
    mocked_url.return_value = valid_url
    mock_connection.return_value = has_connection
    assert can_access_google_page("https://www.google.com/") == result
