from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected_access",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "should return 'Not accessible' if no connection",
        "should return 'Not accessible' if url is not valid",
        "should return 'Not accessible' if no connection and url is not valid",
        "should return 'Accessible' if has connection and url is valid",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        has_connection: bool,
        is_valid_url: bool,
        expected_access: str
) -> None:

    mock_has_internet_connection.return_value = has_connection
    mock_valid_google_url.return_value = is_valid_url
    assert can_access_google_page("https://google.com/") == expected_access
