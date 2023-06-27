import pytest
from unittest import mock

import app.main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,has_connection,result",
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
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        is_valid: bool,
        has_connection: bool,
        result: str
) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page("https://www.google.com") == result