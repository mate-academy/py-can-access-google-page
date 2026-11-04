from unittest.mock import patch
import pytest

# Assuming your test file is placed inside the tests/ or root directory relative to app/main.py
# from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected_result",
    [
        (True, True, "Accessible"),  # Valid URL (200 OK) & Internet available
        (False, True, "Not accessible"),  # Invalid URL (!= 200) & Internet available
        (True, False, "Not accessible"),  # Valid URL (200 OK) & No internet
        (False, False, "Not accessible"),  # Invalid URL (!= 200) & No internet
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
  # Mock the return values of the helper functions
  mock_valid_url.return_value = is_valid_url
  mock_has_internet.return_value = is_connected

  # Call the function under test
  result = can_access_google_page("https://www.google.com")

  # Assert the outcome matches expectations
  assert result == expected_result
