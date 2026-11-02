from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_active, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url,
    mock_has_internet_connection,
    valid_url,
    internet_active,
    expected,
):
    # Configura os retornos simulados para cada cenário
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_active

    result = can_access_google_page("https://www.google.com")
    assert result == expected
