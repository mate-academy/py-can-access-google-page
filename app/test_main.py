from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_page_if_both_are_true(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool
) -> None:

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("google.com") == "Accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page("google.com") == "Not accessible"

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"
