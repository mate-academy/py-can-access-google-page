from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://fake-url.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet_and_invalid_url(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False

    result = can_access_google_page("https://fake-url.com")

    assert result == "Not accessible"
