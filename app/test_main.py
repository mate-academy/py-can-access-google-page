from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrized(
    "url, internet, valid_url, expected",
    [
        (
            "https://www.google.com",
            True,
            True,
            "Accessible"
        ),
        (
            "https://www.google.com",
            True,
            True,
            "Not Accessible"
        ),
        (
            "https://invalid-url.com",
            True,
            True,
            "Not Accessible"
        ),
        (
            "https://invalid-url.com",
            True,
            True,
            "Not Accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_url_function: object,
                                mock_internet_connection: object,
                                url: str,
                                valid_url: bool,
                                internet: bool,
                                expected: str) -> None:
    mock_internet_connection.return_value = internet
    mock_valid_url_function.return_valve = valid_url
    assert can_access_google_page(url) == expected
