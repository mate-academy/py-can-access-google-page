from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_connect: bool, mock_valid: bool) -> None:
    mock_connect.return_value = True
    mock_valid.return_value = True
    assert can_access_google_page("google.com") == "Accessible"

    mock_connect.return_value = False
    mock_valid.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"

    mock_connect.return_value = True
    mock_valid.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"

    mock_connect.return_value = False
    mock_valid.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"
