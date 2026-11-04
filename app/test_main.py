from datetime import datetime
from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_scenarios(
    mock_valid_url,
    mock_has_internet,
    is_valid_url,
    is_connected,
    expected_result,
):
  mock_valid_url.return_value = is_valid_url
  mock_has_internet.return_value = is_connected

  result = can_access_google_page("https://www.google.com")

  assert result == expected_result


@pytest.mark.parametrize(
    "current_time, expected_connection",
    [
        (datetime(2026, 11, 3, 5, 59, 59), False),  # Before boundary
        (datetime(2026, 11, 3, 6, 0, 0), True),  # Lower boundary (inclusive)
        (datetime(2026, 11, 3, 22, 59, 59), True),  # Upper boundary (inclusive)
        (datetime(2026, 11, 3, 23, 0, 0), False),  # After boundary
    ],
)
@patch("app.main.datetime")
def test_internet_connection_time_boundaries(
    mock_datetime, current_time, expected_connection
):
  from app.main import has_internet_connection

  mock_datetime.now.return_value = current_time
  assert has_internet_connection() == expected_connection
