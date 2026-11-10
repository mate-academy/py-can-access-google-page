from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_success(
    mock_valid_url: MagicMock,
    mock_internet_connection: MagicMock,
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_only_connection(
    mock_valid_url: MagicMock,
    mock_internet_connection: MagicMock,
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = False

    assert can_access_google_page("invalid-url") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_only_valid_url(
    mock_valid_url: MagicMock,
    mock_internet_connection: MagicMock,
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_both_false(
    mock_valid_url: MagicMock,
    mock_internet_connection: MagicMock,
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = False

    assert can_access_google_page("invalid-url") == "Not accessible"
