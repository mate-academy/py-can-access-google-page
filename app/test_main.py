from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    result: str = can_access_google_page("https://google.com")

    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_invalid_url(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    result: str = can_access_google_page("https://fake.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_no_internet(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    result: str = can_access_google_page("https://google.com")

    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_both_false(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False

    result: str = can_access_google_page("https://google.com")

    assert result == "Not accessible"
