from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected",
    [
        # Valid URL and internet connection
        ("https://www.google.com", True, True, "Accessible"),
        # Invalid URL but internet connection
        ("https://www.example.com", False, True, "Not accessible"),
        # Valid URL but no internet connection
        ("https://www.google.com", True, False, "Not accessible"),
        # Invalid URL and no internet connection
        ("https://www.example.com", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet_connection: mock.Mock,
    mock_valid_url: mock.Mock,
    url: str,
    valid_url: bool,
    internet_connection: bool,
    expected: str
) -> None:
    # Setting up the mock return values
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection

    # Calling the function with the provided URL
    assert can_access_google_page(url) == expected
