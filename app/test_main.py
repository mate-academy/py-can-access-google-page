from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection(
        mock_has_internet: any,
        mock_valid_url: any
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("http://google.com") == "Not accessible", \
        "You cannot access page if only 'connection' is True."

    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page("http://google.com") == "Not accessible", \
        "You cannot access page if URL is valid but no connection."

    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page("http://google.com") == "Accessible", \
        "Page should be accessible if both URL and connection are valid."
