from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,status",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "both valid_url and connection -> Accessible",
        "no connection -> Not accessible",
        "invalid url -> Not accessible",
        "neither valid url nor connection -> Not accessible",
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessing_google_page_with_different_arguments(
        mock_connection: mock.MagicMock,
        mock_valid_url: mock.MagicMock,
        has_connection: bool,
        valid_url: bool,
        status: str
) -> None:
    mock_connection.return_value = has_connection
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("url") == status
