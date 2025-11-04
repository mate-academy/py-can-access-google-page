from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_internet: mock.MagicMock,
    mock_valid: mock.MagicMock
) -> None:
    """Test when both internet and URL are valid."""
    mock_internet.return_value = True
    mock_valid.return_value = True

    result: str = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
    mock_internet: mock.MagicMock,
    mock_valid: mock.MagicMock
) -> None:
    """Test when URL is invalid but internet is available."""
    mock_internet.return_value = True
    mock_valid.return_value = False

    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
    mock_internet: mock.MagicMock,
    mock_valid: mock.MagicMock
) -> None:
    """Test when internet is unavailable but URL is valid."""
    mock_internet.return_value = False
    mock_valid.return_value = True

    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url_and_no_internet(
    mock_internet: mock.MagicMock,
    mock_valid: mock.MagicMock
) -> None:
    """Test when both internet and URL are invalid."""
    mock_internet.return_value = False
    mock_valid.return_value = False

    result: str = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
