from unittest import mock
from app.main import can_access_google_page


def test_valid_url_and_connection_exists() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=True),
        mock.patch("app.main.has_internet_connection", return_value=True)
    ):
        assert can_access_google_page(
            "https://translate.google.com/"
            "?hl=ru&sl=en&tl=ru&op=translate") == "Accessible"


def test_invalid_url_not_accessible() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=False),
        mock.patch("app.main.has_internet_connection", return_value=True)
    ):
        assert can_access_google_page("") == "Not accessible"


def test_no_internet_connection_not_accessible() -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=True),
        mock.patch("app.main.has_internet_connection", return_value=False)
    ):
        assert can_access_google_page(
            "https://translate.google.com/?hl=ru&"
            "sl=en&tl=ru&op=translate") == "Not accessible"
