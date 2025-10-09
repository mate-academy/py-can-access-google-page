from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(
    mocked_internet_connection: MagicMock,
    mocked_valid_google_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_with("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_without_internet_connection(
    mocked_internet_connection: MagicMock,
    mocked_valid_google_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_not_called()
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_with_invalid_google_url(
    mocked_internet_connection: MagicMock,
    mocked_valid_google_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_with_invalid_url_without_internet_connection(
    mocked_internet_connection: MagicMock,
    mocked_valid_google_url: MagicMock
) -> None:
    result = can_access_google_page("https://google.com")
    mocked_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_not_called()
    assert result == "Not accessible"
