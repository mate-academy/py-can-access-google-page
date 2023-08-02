from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    test_cases = [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invalidurl.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible")
    ]

    for url, has_internet, is_valid, expected_result in test_cases:
        mock_valid_google_url.return_value = is_valid
        mock_has_internet_connection.return_value = has_internet

        result = can_access_google_page(url)

        assert result == expected_result
