from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test1_can_access_page_when_connection_and_url_are_valid(
        mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    url_test = "https://www.google.com"
    result = can_access_google_page(url_test)
    assert result == "Accessible"

    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with(url_test)


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test2_can_access_page_when_connection_and_url_are_valid(
        mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    url_test = "https://www.google.com"
    result = can_access_google_page(url_test)
    assert result == "Not accessible"

    mock_valid_url.assert_not_called()

@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test3_can_access_page_when_connection_and_url_are_valid(
        mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    url_test = "https://www.google.com"
    result = can_access_google_page(url_test)
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)


def test4_can_access_page_when_connection_and_url_are_valid(
        mock_valid_url: MagicMock, mock_has_internet: MagicMock) -> None:
    url_test = "https://www.google.com"
    result = can_access_google_page(url_test)
    assert result == "Not accessible"
