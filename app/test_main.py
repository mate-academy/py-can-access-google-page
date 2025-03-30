from app.main import can_access_google_page
import pytest
from typing import Callable
from unittest import mock

Google = "https://google.com/"


@pytest.mark.parametrize(
    "has_internet, has_valid, message",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "if both are True return 'Accessible'",
        "if has no internet connection return 'Not accessible'",
        "if url is not valid  return 'Not accessible'",
        "if both are False return 'Not accessible'"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_has_internet_connection: Callable,
    mock_valid_google_url: Callable,
    has_internet: bool,
    has_valid: bool,
    message: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = has_valid
    assert can_access_google_page(Google) == message
