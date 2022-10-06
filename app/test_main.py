from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_valid_with_connection(
        mock_valid_google_url: bool,
        mock_internet_connection: bool
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("Google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_not_connection_and_not_valid(
        mock_valid_google_url: bool,
        mock_internet_connection: bool
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page("Google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_with_connection_not_valid_page(
        mock_valid_google_url: bool,
        mock_internet_connection: bool
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("Google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_without_connection_but_valid_page(
        mock_valid_google_url: bool,
        mock_internet_connection: bool
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("Google.com") == "Not accessible"
