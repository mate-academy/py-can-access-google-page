from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_connection_and_url_are_valid(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_no_internet_connection(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_is_invalid(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_both_conditions_fail(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = False

    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"
