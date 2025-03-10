import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet, mock_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "You have the access to thr website",
        "Invalid URL for accessing the google.com",
        "You have no internet connection",
        "No internet connection and invalid URL",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessing_google_page(
        mock_valid_url: bool,
        mock_has_internet_connection: bool,
        mock_internet: bool,
        mock_url: bool,
        expected: str
) -> None:
    mock_has_internet_connection.return_value = mock_internet
    mock_valid_url.return_value = mock_url
    result = can_access_google_page("http://www.google.com")
    assert result == expected