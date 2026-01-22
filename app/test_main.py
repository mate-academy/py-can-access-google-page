import pytest
from unittest.mock import patch, Mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_has_internet,mock_valid_url,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_correctly(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
    mock_has_internet: bool,
    mock_valid_url: bool,
    expected: str
) -> None:
    mock_has_internet_connection.return_value = mock_has_internet
    mock_valid_google_url.return_value = mock_valid_url
    url = "http://www.google.com"
    assert can_access_google_page(url) == expected
