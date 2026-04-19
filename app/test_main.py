from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_url: str,
                                mock_has_connection: str) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"

    mock_has_connection.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"

    mock_has_connection.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("https://bad-url.com") == "Not accessible"

    mock_has_connection.return_value = False
    mock_valid_url.return_value = False
    assert can_access_google_page("https://any-url.com") == "Not accessible"
