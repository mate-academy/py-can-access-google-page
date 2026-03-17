from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize("valid_url, has_connection, expected_result", [
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
    (True, True, "Accessible")
])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_success(
        mock_valid: mock.MagicMock,
        mock_internet: mock.MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str) -> None:
    mock_valid.return_value = valid_url
    mock_internet.return_value = has_connection
    assert can_access_google_page("https://any-url.com") == expected_result
