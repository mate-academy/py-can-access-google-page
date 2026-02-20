from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        has_internet_connection: mock.MagicMock,
        valid_page: mock.MagicMock
) -> None:
    valid_page.return_value = True
    has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_link(
        has_internet_connection: mock.MagicMock,
        valid_page: mock.MagicMock
) -> None:
    has_internet_connection.return_value = True
    valid_page.return_value = False
    assert can_access_google_page("unknown_line") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_no_connection(
        has_internet_connection: mock.MagicMock,
        valid_page: mock.MagicMock
) -> None:
    has_internet_connection.return_value = False
    valid_page.return_value = True
    assert (can_access_google_page(
        "https://www.google.com/") == "Not accessible"
    )
