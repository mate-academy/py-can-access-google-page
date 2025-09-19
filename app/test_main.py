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
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(mock_has_internet_connection: Mock,
                                mock_valid_google_url: Mock,
                                has_internet_connection: bool,
                                valid_google_url: str,
                                expected: bool) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("url") == expected
