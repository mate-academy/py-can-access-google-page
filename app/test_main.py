from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: bool,
    mock_valid_google_url: bool,
) -> None:
    test_cases = [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]

    for valid_url, has_connection, expected in test_cases:
        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = has_connection

        assert can_access_google_page("https://www.google.com") == expected
