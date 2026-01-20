from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "has_internet_connection, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_url(
    mock_valid_url: mock,
    mock_has_internet_connection: mock, valid_url: bool,
        has_internet_connection: bool, expected_result: str) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("www.google.com") == expected_result
