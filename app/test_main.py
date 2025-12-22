from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_test_connect:
        yield mock_test_connect


@pytest.fixture()
def mock_valid() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_test_valid:
        yield mock_test_valid


@pytest.mark.parametrize(
    "connect_check, valid_check, value",
    [
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "No connection, Invalid URL",
        "Connected, Valid URL",
        "Connected, Invalid URL",
        "No connection, Valid URL"
    ]
)
def test_can_access_google_page(
        mock_connection: mock.Mock,
        mock_valid: mock.Mock,
        connect_check: bool,
        valid_check: bool,
        value: str
) -> None:
    mock_connection.return_value = connect_check
    mock_valid.return_value = valid_check
    assert can_access_google_page("example.com") == value
