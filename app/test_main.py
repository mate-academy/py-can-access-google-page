from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, is_valid, expected_output",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invald-url.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        internet_connection: bool,
        is_valid: bool,
        expected_output: str
) -> None:
    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        mock_valid_google_url.return_value = is_valid
        mock_has_internet_connection.return_value = internet_connection

        assert can_access_google_page(url) == expected_output
