from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
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
            False,
            "Not accessible"
        ),
        (
            "https://www.google.com",
            False,
            True,
            "Not accessible"
        ),
        (
            "https://www.google.com",
            False,
            False,
            "Not accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_url_function: object,
                                mock_internet_connection: object,
                                url: str,
                                internet: bool,
                                valid_url: bool,
                                expected: str) -> None:
    mock_internet_connection.return_value = internet
    mock_valid_url_function.return_value = valid_url
    assert can_access_google_page(url) == expected
