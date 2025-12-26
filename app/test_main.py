from unittest.mock import patch


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(has_internet_connection: str,
                                valid_google_url: str) -> None:
    has_internet_connection.return_value = True
    valid_google_url.return_value = True
    test_url = "http://www.google.com"
    result = can_access_google_page(test_url)
    assert result == "Accessible"
    valid_google_url.assert_called_once()
    valid_google_url.assert_called_once_with(test_url)
    has_internet_connection.assert_called_once()
