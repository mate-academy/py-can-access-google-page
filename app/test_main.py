from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible_when_url_valid_and_connection_exists(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.not-google.com")

    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_no_internet_connection(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_url_invalid_and_no_connection(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.not-google.com")

    assert result == "Not accessible"
