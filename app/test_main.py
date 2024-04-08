from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        ("https://www.google.com", True, "Accessible"),
        ("https://non-existent_google.com", True, "Not accessible"),
        ("https://www.google.com", False, "Not accessible"),
        ("https://non-existent_google.com", False, "Not accessible")
    ],
    ids=["Existing URL, is internet connection",
         "Non-existent URL, is internet connection",
         "Existing URL, no internet connection",
         "Non-existent URL, no internet connection"]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
    internet_connection: bool,
    expected_result: str
):
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = internet_connection

    assert can_access_google_page("https://www.google.com") == expected_result

    mock_has_internet_connection.assert_called_once()
    if internet_connection:
        mock_valid_google_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_google_url.assert_not_called()
