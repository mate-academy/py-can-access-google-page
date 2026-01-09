from unittest.mock import patch, MagicMock


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_both_function_are_true(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_internet_connection_are_false(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_google_url_are_false(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"
