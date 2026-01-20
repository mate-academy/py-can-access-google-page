from unittest.mock import patch, MagicMock
import pytest

import app.main


@pytest.mark.parametrize(
    "valid_url, valid_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "connection_and_url_is_true",
        "only_connection_is_true",
        "only_url_is_true"
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mocked_google_url: MagicMock,
    mocked_internet_connection: MagicMock,
    valid_url: bool,
    valid_connection: bool,
    expected_result: str
) -> None:
    mocked_google_url.return_value = valid_url
    mocked_internet_connection.return_value = valid_connection
    assert app.main.can_access_google_page("url") == expected_result
