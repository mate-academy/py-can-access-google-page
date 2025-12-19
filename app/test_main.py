from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    url = "https://www.google.com"

    result = can_access_google_page(url)

    assert result == "Accessible"
    mock_valid_url.assert_called_once_with(url)
    mock_has_internet.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    url = "https://www.notgoogle.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
