from unittest.mock import patch, Mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_google_url,"
                         "has_internet_connection,"
                         "expected", [
                             (True, True, "Accessible"),
                             (False, False, "Not accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                         ])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists_returns_accessible(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        valid_google_url: str,
        has_internet_connection: bool,
        expected: bool) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("url") == expected
