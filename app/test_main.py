from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_with_valid_url_and_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("valid_url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_with_invalid_url_and_no_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("valid_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_with_valid_url_and_no_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("valid_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_with_invalid_url_and_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("valid_url") == "Not accessible"
