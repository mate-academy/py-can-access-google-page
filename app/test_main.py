import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_return,internet_connection,expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
    ]
)
def test_for_the_correct_meaning_of_url_and_connection(
        valid_url_return: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    with (patch("app.main.valid_google_url")
          as mock_valid_url,
            patch("app.main.has_internet_connection")
            as mock_internet_connection):
        mock_valid_url.return_value = valid_url_return
        mock_internet_connection.return_value = internet_connection
        assert can_access_google_page(
            "https://www.google.com"
        ) == expected_result
