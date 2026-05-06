from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible_when_url_is_valid_and_internet_exists(
    mock_has_internet: MagicMock  ,
    mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_url_is_invalid(
    mock_has_internet: MagicMock  ,
    mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("https://invalid.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_no_internet_connection(
    mock_has_internet: MagicMock  ,
    mock_valid_url: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
