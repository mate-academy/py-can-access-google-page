from unittest.mock import patch

from app.main import can_access_google_page


def test_can_access_google_page():
    with (
        patch("app.main.valid_google_url") as mock_valid_url,
        patch("app.main.has_internet_connection") as mock_internet_conection,
    ):
        mock_valid_url.return_value = True
        mock_internet_conection.return_value = True
        assert (
            can_access_google_page("https://www.google.com") == "Accessible"
        )

        mock_valid_url.return_value = False
        mock_internet_conection.return_value = True
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )

        mock_valid_url.return_value = True
        mock_internet_conection.return_value = False
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )

        mock_valid_url.return_value = False
        mock_internet_conection.return_value = False
        assert (
            can_access_google_page("https://www.google.com")
            == "Not accessible"
        )
