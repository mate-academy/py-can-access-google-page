from unittest import mock
import pytest
from app.main import can_access_google_page


VALID_URL = "https://www.google.com"
INVALID_URL = "https://www.invalid-url.com"


@pytest.mark.parametrize(
    "valid_url_return, internet_connection_return, url,"
    " expected_result, error_message",
    [
        (True, True, VALID_URL, "Accessible",
         "Failed when both URL and connection are valid"),
        (True, False, VALID_URL, "Not accessible",
         "Failed when URL is valid but no internet connection"),
        (False, True, INVALID_URL, "Not accessible",
         "Failed when URL is invalid but internet connection exists"),
        (False, False, INVALID_URL, "Not accessible",
         "Failed when both URL and connection are invalid"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet_connection: mock.Mock, mock_valid_url: mock.Mock,
    valid_url_return: bool, internet_connection_return: bool,
    url: str, expected_result: str, error_message: str
) -> None:
    mock_valid_url.return_value = valid_url_return
    mock_internet_connection.return_value = internet_connection_return

    assert can_access_google_page(url) == expected_result, error_message
