from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_all_good(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_url_not_valid(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://not_found.com/") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_no_internet_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_url_is_not_valid_and_no_internet_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://not_found.com/") == "Not accessible"
