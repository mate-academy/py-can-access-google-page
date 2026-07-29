from unittest.mock import MagicMock, patch

from app.main import can_access_google_page



@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet_and_invalid_url(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
