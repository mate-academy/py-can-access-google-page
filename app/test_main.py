from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com/")

    assert result == "Accessible"
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("https://www.google.com/")
