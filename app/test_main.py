from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "url,is_valid_url,has_connection,expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_has_internet_connection: mock.Mock ,
        url: str,
        is_valid_url: bool,
        has_connection: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page(url) == expected_result
