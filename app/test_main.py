from unittest.mock import patch, MagicMock


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_walid_url_and_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_page_without_internet_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_invalid_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"
