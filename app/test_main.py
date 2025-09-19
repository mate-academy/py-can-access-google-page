from unittest import mock


from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
            as mock_has_internet_connection):
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("url")

        assert result == "Accessible"
        mock_valid_google_url.assert_called_once_with("url")
        mock_has_internet_connection.assert_called_once()
