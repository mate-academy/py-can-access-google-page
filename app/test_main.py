from unittest import mock

import app.main


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_valid_and_has_internet(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = app.main.can_access_google_page("https://google.com")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_when_only_connection_exists(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = app.main.can_access_google_page("https://youtube.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_when_only_url_is_valid(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = app.main.can_access_google_page("https://google.com")
    assert result == "Not accessible"
