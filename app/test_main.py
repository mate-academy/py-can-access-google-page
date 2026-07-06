import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
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
        mock_has_internet_connection: mock.Mock,
        mock_valid_google_url: mock.Mock,
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
