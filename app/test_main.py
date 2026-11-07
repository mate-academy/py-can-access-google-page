from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
    mock_valid_url: mock.MagicMock,
    mock_has_connection: mock.MagicMock,
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_no_connection(
    mock_valid_url: mock.MagicMock,
    mock_has_connection: mock.MagicMock,
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
    mock_valid_url: mock.MagicMock,
    mock_has_connection: mock.MagicMock,
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://invalid-url.com") == "Not accessible"
    )


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection(
    mock_valid_url: mock.MagicMock,
    mock_has_connection: mock.MagicMock,
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://invalid-url.com") == "Not accessible"
    )
