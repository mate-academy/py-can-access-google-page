from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_success(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_failed_valid(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_failed_internet(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = True
    mock_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_failed_both(
        mock_valid: MagicMock,
        mock_internet: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()
