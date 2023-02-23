from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_only_valid_url(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_only_connection(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection(
        mock_valid_url: bool,
        mock_connection: bool
) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
