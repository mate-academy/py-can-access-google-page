from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page_with_internet_check():
    with mock.patch("app.main.valid_google_url") as mock_valid, \
            mock.patch("app.main.has_internet_connection") as mock_internet:
        mock_valid.return_value = True
        mock_internet.return_value = True

        result = can_access_google_page("https://mate.academy/")
        assert result == "Accessible"


def test_can_not_access_google_page_with_internet_check():
    with mock.patch("app.main.valid_google_url") as mock_valid, \
            mock.patch("app.main.has_internet_connection") as mock_internet:
        mock_valid.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://mate.academy/")
        assert result == "Not accessible"
