from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet, valid, expected_output",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://invalid.url", True, False, "Not accessible"),
        ("http://www.google.com", False, True, "Not accessible"),
        ("", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(url: str,
                                internet: bool,
                                valid: bool,
                                expected_output: str) -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_connection:
        mock_internet_connection.return_value = internet
        mock_valid_url.return_value = valid
        assert can_access_google_page(url) == expected_output
