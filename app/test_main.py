from unittest import mock
from app import main


def test_can_access_google_page() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_con:
        with mock.patch("app.main.valid_google_url") as mock_url:
            mock_con.return_value = True
            mock_url.return_value = True

            assert main.can_access_google_page("something") == "Accessible"


def test_cannot_access_if_only_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_con:
        with mock.patch("app.main.valid_google_url") as mock_url:
            mock_con.return_value = True
            mock_url.return_value = False

            assert main.can_access_google_page("something") == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_con:
        with mock.patch("app.main.valid_google_url") as mock_url:
            mock_con.return_value = False
            mock_url.return_value = True

            assert main.can_access_google_page("something") == "Not accessible"


def test_cannot_access_if_nothing_is_valid() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_con:
        with mock.patch("app.main.valid_google_url") as mock_url:
            mock_con.return_value = False
            mock_url.return_value = False

            assert main.can_access_google_page("something") == "Not accessible"
