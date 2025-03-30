from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: any, mock_valid_url: any
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert (
        can_access_google_page("https://www.google.com") == "Accessible"
    ), ("Expected 'Accessible' when both valid_google_url "
        "and has_internet_connection return True")

    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert (
        can_access_google_page("https://www.google.com") == "Not accessible"
    ), ("Expected 'Not accessible' when valid_google_url returns False, "
        "even if has_internet_connection is True")

    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert (
        can_access_google_page("https://www.google.com") == "Not accessible"
    ), ("Expected 'Not accessible' when has_internet_connection returns False,"
        " even if valid_google_url is True")

    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert (
        can_access_google_page("https://www.google.com") == "Not accessible"
    ), ("Expected 'Not accessible' when both valid_google_url and"
        " has_internet_connection return False")
