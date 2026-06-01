from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_connection_exists(
    mock_url: MagicMock,
    mock_connection: MagicMock
) -> None:
    result = can_access_google_page("test_str")
    assert result == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_no_internet_connection(
    mock_url: MagicMock,
    mock_connection: MagicMock
) -> None:
    result = can_access_google_page("test_str")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url(
    mock_url: MagicMock,
    mock_connection: MagicMock
) -> None:
    result = can_access_google_page("test_str")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_no_connection(
    mock_url: MagicMock,
    mock_connection: MagicMock
) -> None:
    result = can_access_google_page("test_str")
    assert result == "Not accessible"
