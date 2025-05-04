from app.main import can_access_google_page
from unittest.mock import patch, MagicMock


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_accessible_when_url_valid_and_internet_on(
    mock_internet: MagicMock,
    mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://shmoogle.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_not_accessible_when_url_invalid(
    mock_net: MagicMock,
    mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://shmoogle.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_when_no_internet(
    mock_net: MagicMock,
    mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://shmoogle.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_when_both_invalid(
    mock_net: MagicMock,
    mock_url: MagicMock
) -> None:
    result = can_access_google_page("https://shmoogle.com")
    assert result == "Not accessible"
