import pytest
from unittest.mock import patch, Mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,valid_google_url,expected, test_id",
    [
        (True, True, "Accessible",
         "If you have valid URL and internet connection, "
         "return 'Accessible' "),
        (True, False, "Not accessible",
         "If you have not valid URL, return 'Not accessible'"),
        (False, True, "Not accessible",
         "If you do not have internet connection, return 'Not accessible' "),
        (False, False, "Not accessible",
         "If you have not valid URL and do not have internet connection, "
         "return 'Not accessible'"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        has_internet: bool,
        valid_google_url: bool,
        expected: str,
        test_id: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("www.google.com") == expected, test_id
