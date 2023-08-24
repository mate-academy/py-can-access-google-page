from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:

    test_url = "https://www.google.com"
    test_data = [
        [True, True, "Accessible"],
        [False, True, "Not accessible"],
        [True, False, "Not accessible"],
        [False, False, "Not accessible"]
    ]

    for (
            mock_valid_google_url.return_value,
            mock_has_internet_connection.return_value,
            expected_result
    ) in test_data:

        assert can_access_google_page(test_url) == expected_result
