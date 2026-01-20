import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_valid_url, mock_internet, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ],
    ids=[
        "Function should return Accessible when all good",
        "Function should return not accessible when has no internet",
        "Function should return not accessible when url is invalid",
        ("Function should return not accessible"
         " when has no internet and url is invalid"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_url_function: object,
                                mock_internet_connection: object,
                                url: str,
                                mock_valid_url: bool,
                                mock_internet: bool,
                                expected: str) -> None:
    mock_valid_url_function.return_value = mock_valid_url
    mock_internet_connection.return_value = mock_internet
    assert can_access_google_page(url) == expected
