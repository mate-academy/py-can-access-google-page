from unittest import mock
from typing import Any
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "valid_url,intern_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet_connection: Any,
    mock_valid_url: Any,
    valid_url: bool,
    intern_connection: bool,
    result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = intern_connection
    assert can_access_google_page("https://www.google.com") == result
