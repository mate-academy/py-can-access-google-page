import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_result: str
) -> None:

    test_url = "https://www.google.com"

    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection

    assert can_access_google_page(test_url) == expected_result
