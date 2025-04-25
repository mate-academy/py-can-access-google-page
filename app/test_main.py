from unittest import mock

from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_connection_exists(
        mock_has_connection: Any,
        mock_valid_url: Any
) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)

    assert result == "Accessible"
    mock_has_connection.assert_called_once()
    mock_valid_url.assert_called_once_with(url)
