from unittest.mock import patch
import pytest

# Assuming the function can_access_google_page is imported from your application module:
# from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected_result",
    [
        (True, True, "Accessible"),  # Valid URL & Internet available
        (False, True, "Not accessible"),  # Invalid URL & Internet available
        (True, False, "Not accessible"),  # Valid URL & No internet
        (False, False, "Not accessible"),  # Invalid URL & No internet
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def class_test_can_access_google_page(
    mock_valid_url,
    mock_has_internet,
    is_valid_url,
    is_connected,
    expected_result,
):
  mock_valid_url.return_value = is_valid_url
  mock_has_internet.return_value = is_connected

  # Replace 'https://www.google.com' with any test URL string
  result = can_access_google_page("https://www.google.com")

  assert result == expected_result
