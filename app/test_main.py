from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
def test_when_url_valid(mock_google_url: mock) -> None:
    mock_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
def test__when_time_internet(mock_has_connection: mock) -> None:
    mock_has_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
def test_when_url_not_valid(mock_google_url: mock) -> None:
    mock_google_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_when_not_time_internet(mock_has_connection: mock) -> None:
    mock_has_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
