from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_when_url_is_valid_and_has_internet(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_is_invalid(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.notgoogle.com")

    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid_and_no_internet(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    result = can_access_google_page("https://www.notgoogle.com")

    assert result == "Not accessible"
