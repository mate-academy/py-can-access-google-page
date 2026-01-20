from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid url is True, Internet connection is True",
        "Valid url is True, Internet connection is False",
        "Valid url is False, Internet connection is True",
        "Valid url is False, Internet connection is False",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_google_url: MagicMock,
    mock_has_connection: MagicMock,
    valid_url: bool,
    connection: bool,
    access: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_connection.return_value = connection
    assert can_access_google_page("google.com") == access
