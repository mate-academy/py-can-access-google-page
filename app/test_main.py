from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_with_has_internet_connection_is_false(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://facebook.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_with_valid_google_url_is_false(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://facebook.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_with_valid_google_url_and_has_internet_connection_is_false(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://facebook.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_with_valid_google_url_and_has_internet_connection_is_true(
        mock_has_internet_connection: str,
        mock_valid_google_url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://facebook.com") == "Accessible"
