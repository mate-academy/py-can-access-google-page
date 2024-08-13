import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_valid_google_url_return, "
    "mock_has_internet_connection_return, "
    "expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.invalid-url.com", False, True, "Not accessible"),
        ("https://www.invalid-url.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        url: str,
        mock_valid_google_url_return: bool,
        mock_has_internet_connection_return: bool,
        expected_result: str
) -> None:
    with (
        patch("app.main.has_internet_connection")
        as mock_has_internet_connection,
        patch("app.main.valid_google_url")
        as mock_valid_google_url
    ):
        mock_valid_google_url.return_value = mock_valid_google_url_return
        mock_has_internet_connection.return_value = (
            mock_has_internet_connection_return
        )

        assert can_access_google_page(url) == expected_result
