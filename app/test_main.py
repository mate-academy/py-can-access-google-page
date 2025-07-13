from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_main_func(mock_has_internet: bool, mock_valid: bool) -> None:
    mock_valid.return_value = True
    mock_has_internet.return_value = True
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == "Accessible"

    mock_valid.return_value = False
    mock_has_internet.return_value = False
    result = can_access_google_page("https://www.google.com.u/")
    assert result == "Not accessible"

    mock_valid.return_value = True
    mock_has_internet.return_value = False
    result = can_access_google_page("https://www.google.com.u/")
    assert result == "Not accessible"

    mock_valid.return_value = False
    mock_has_internet.return_value = True
    result = can_access_google_page("https://www.google.com.u/")
    assert result == "Not accessible"
