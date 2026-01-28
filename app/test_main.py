from app.main import can_access_google_page
from unittest.mock import patch, Mock

url = "https://google.com"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_to_google_is_available(mock_has_internet_connection: Mock,
                                       mock_valid_google_url: Mock) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    expected = "Accessible"
    actual = can_access_google_page(url)
    assert actual == expected
