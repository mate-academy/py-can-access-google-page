from unittest import mock

from app.main import can_access_google_page


def test_should_return_right_answer() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url, \
            mock.patch("app.main.has_internet_connection")\
            as mock_has_internet_connection:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"

        mock_has_internet_connection.return_value = False
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        result = can_access_google_page("https://www.invalidurl.com")
        assert result == "Not accessible"
