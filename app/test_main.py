import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_connection: mock.Mock,
        mock_valid_url: mock.Mock,
        has_connection: bool,
        is_valid_url: bool,
        expected_result: str,
) -> None:
    mock_connection.return_value = has_connection
    mock_valid_url.return_value = is_valid_url

    assert can_access_google_page("url") == expected_result
