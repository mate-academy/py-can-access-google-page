from unittest import mock

from .main import can_access_google_page


def test_can_access_to_google_page_when_accessible() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid:
        with mock.patch("app.main.has_internet_connection") as mock_internet:
            mock_internet.return_value = True
            mock_valid.return_value = True
            result = can_access_google_page("https://google.com")
            assert result == "Accessible"

def test_can_access_google_page_when_not_accessible() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid:
        with mock.patch("app.main.has_internet_connection") as mock_internet:
            mock_internet.return_value = False
            mock_valid.return_value = False
            result = can_access_google_page("https://google.com")
            assert result == "Not accessible"
