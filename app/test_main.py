from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_url: bool,
                                mock_internet: bool) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_without_internet(mock_url: bool,
                                     mock_internet: bool) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_url_is_error(mock_url: bool,
                                 mock_internet: bool) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
