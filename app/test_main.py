from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch("app.main.has_internet_connection") as hic:
        with mock.patch("app.main.valid_google_url") as vgu:
            hic.return_value = True
            vgu.return_value = True
            result = can_access_google_page("http://www.google.com")
            assert result == "Accessible"


def test_cannot_access_if_only_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as hic:
        with mock.patch("app.main.valid_google_url") as vgu:

            hic.return_value = True
            vgu.return_value = False
            result = can_access_google_page("http://www.google.com")
            assert result == "Not accessible"


def test_cannot_access_if_only_valid_url() -> None:
    with mock.patch("app.main.has_internet_connection") as hic:
        with mock.patch("app.main.valid_google_url") as vgu:

            hic.return_value = False
            vgu.return_value = True
            result = can_access_google_page("http://www.google.com")
            assert result == "Not accessible"
