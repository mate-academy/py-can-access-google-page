from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_all_valid(
        mock_valid_internet: MagicMock,
        mock_valid_url: MagicMock) -> None:
    mock_valid_internet.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_only_internet_valid(
        mock_valid_internet: MagicMock,
        mock_valid_url: MagicMock) -> None:
    mock_valid_internet.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_only_url_valid(
        mock_valid_internet: MagicMock,
        mock_valid_url: MagicMock) -> None:
    mock_valid_internet.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_both_invalid(
        mock_valid_internet: MagicMock,
        mock_valid_url: MagicMock) -> None:
    mock_valid_internet.return_value = False
    mock_valid_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
