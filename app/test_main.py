import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet_conn, expected_result",
    [
        (True, True, "Accessible"),      # Oba warunki spełnione
        (True, False, "Not accessible"),     # Brak internetu
        (False, True, "Not accessible"),     # Błędny URL
        (False, False, "Not accessible"),    # Nic nie działa
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
    url_valid: bool,
    internet_conn: bool,
    expected_result: str
) -> None:
    mock_valid_url.return_value = url_valid
    mock_has_internet.return_value = internet_conn

    result = can_access_google_page("https://google.com")

    assert result == expected_result
