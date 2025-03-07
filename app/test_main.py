import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet, mock_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Everything works correctly",
        "Invalid URL for accessing the Google home page",
        "It has no internet connection",
        "No internet connection and invalid URL",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet: bool,
                                mock_valid_url: bool,
                                mock_internet: bool,
                                mock_url: bool,
                                expected_result: str) -> None:
    mock_has_internet.return_value = mock_internet
    mock_valid_url.return_value = mock_url
    result = can_access_google_page("http://www.google.com")
    assert result == expected_result
