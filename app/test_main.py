from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_google(
        mock_valid_google_url: MagicMock ,
        mock_has_internet_connection: MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:

    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection

    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
