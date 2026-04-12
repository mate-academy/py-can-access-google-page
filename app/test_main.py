from unittest import mock
from app import main


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
        mock_valid_url: mock.MagicMock,
        mock_has_connection: mock.MagicMock
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = True

    actual_result = main.can_access_google_page("https://google.com")
    assert actual_result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
        mock_valid_url: mock.MagicMock,
        mock_has_connection: mock.MagicMock
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = True

    actual_result = main.can_access_google_page("https://google.com")
    assert actual_result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
        mock_valid_url: mock.MagicMock,
        mock_has_connection: mock.MagicMock
) -> None:
    mock_has_connection.return_value = True
    mock_valid_url.return_value = False

    actual_result = main.can_access_google_page("https://invalid-url.com")
    assert actual_result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_both_fail(
        mock_valid_url: mock.MagicMock,
        mock_has_connection: mock.MagicMock,
) -> None:
    mock_has_connection.return_value = False
    mock_valid_url.return_value = False

    actual_result = main.can_access_google_page("https://invalid-url.com")
    assert actual_result == "Not accessible"
