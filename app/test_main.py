import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("url, valid_url, internet_connection, expected_result", [ # Noqa E501
    ("https://www.google.com", True, True, "Accessible"),
    ("invalid_url", False, False, "Not accessible"),
    ("https://www.google.com", False, True, "Not accessible"),
    ("https://www.google.com", True, False, "Not accessible"),
])
@patch("your_module.valid_google_url")
@patch("your_module.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection, mock_valid_google_url, url, valid_url, internet_connection, expected_result): # Noqa E501
    mock_valid_google_url.return_value = valid_url

    # Mock the has_internet_connection function
    mock_has_internet_connection.return_value = internet_connection

    # Call the function with the provided URL
    result = can_access_google_page(url)

    # Assert that the result matches the expected result
    assert result == expected_result


if __name__ == "__main__":
    pytest.main()

