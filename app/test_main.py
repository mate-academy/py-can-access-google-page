from app.main import can_access_google_page
from unittest import mock


def test_if_both_func_true():
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_url
    ):
        mock_connection.return_value = True
        mock_url.return_value = True
        assert can_access_google_page("url") == "Accessible"


def test_has_internet_connection_is_false():
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_url
    ):
        mock_connection.return_value = False
        mock_url.return_value = True
        assert can_access_google_page("url") == "Not accessible"


def test_valid_google_url_is_false():
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_url
    ):
        mock_connection.return_value = True
        mock_url.return_value = False
        assert can_access_google_page("url") == "Not accessible"

def test_if_both_func_false():
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_url
    ):
        mock_connection.return_value = False
        mock_url.return_value = False
        assert can_access_google_page("url") == "Not accessible"
