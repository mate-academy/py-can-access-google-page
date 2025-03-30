import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "internet_connection, google_url_valid, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_has_internet_connection: bool,
    mock_valid_google_url: bool,
    internet_connection: bool,
    google_url_valid: bool,
    expected: bool
) -> None:
    """
    Test the can_access_google_page function by mocking dependencies.
    """
    # Mock the return values of the dependencies
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = google_url_valid

    # Call the function with a dummy URL
    url = "http://www.google.com"
    result = can_access_google_page(url)

    # Assert the result matches the expected value
    assert result == expected
