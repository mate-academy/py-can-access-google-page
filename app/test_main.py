from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_returns_accessible_when_both_true(
        mock_internet_connection: bool,
        mock_google_url: bool) -> None:
    mock_internet_connection.return_value = True
    mock_google_url.return_value = True
    assert can_access_google_page("url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_returns_not_accessible_when_no_internet(
        mock_internet_connection: bool,
        mock_google_url: bool) -> None:
    mock_internet_connection.return_value = False
    mock_google_url.return_value = True
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_returns_not_accessible_when_not_valid_url(
        mock_internet_connection: bool,
        mock_google_url: bool) -> None:
    mock_internet_connection.return_value = True
    mock_google_url.return_value = False
    assert can_access_google_page("url") == "Not accessible"
