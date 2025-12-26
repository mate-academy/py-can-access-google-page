from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_when_valid_url_and_connection_exists(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url_and_connection_exists(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://inval-url.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_valid_url_and_no_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url_and_no_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://inval-url.com") == "Not accessible"
