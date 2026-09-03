from unittest import mock

from app import main


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
    mock_internet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True

    result = main.can_access_google_page("https://google.com")

    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exists(
    mock_internet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False

    result = main.can_access_google_page("https://google.com")

    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
    mock_internet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True

    result = main.can_access_google_page("https://google.com")

    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_no_connection(
    mock_internet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False

    result = main.can_access_google_page("https://google.com")

    assert result == "Not accessible"
