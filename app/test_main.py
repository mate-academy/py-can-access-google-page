from app.main import can_access_google_page
import pytest
from typing import Callable
from unittest import mock

LINK = "https://mail.google.com/"


@pytest.mark.parametrize(
    "has_internet, has_valid, res_message",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "if all conditions -> True <- must return 'Accessible'",
        "if 'has_internet_con' -> False <- must return 'Not accessible'",
        "if 'valid_google_url' -> False <- must return 'Not accessible'",
        "if all conditions -> False <- must return 'Not accessible'"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_has_internet_connection: Callable,
    mock_valid_google_url: Callable,
    has_internet: bool,
    has_valid: bool,
    res_message: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = has_valid
    assert can_access_google_page(LINK) == res_message
