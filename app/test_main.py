from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def valid_internet_page() -> str:
    return "https://www.google.com"


@pytest.fixture
def wrong_internet_page() -> str:
    return "https://www.Gwwosdfgle.caaam"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
# Success case
def test_can_access_google_page_success(
        mock_has_internet: mock.Mock,
        mock_valid_google_url: mock.Mock,
        valid_internet_page: str
) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page(valid_internet_page)
    assert result == "Accessible"
    mock_has_internet.assert_called_once()
    mock_valid_google_url.assert_called_once_with(valid_internet_page)


@mock.patch("app.main.has_internet_connection")
def test_failed_internet_connection(mock_has_internet: mock.Mock,
                                    valid_internet_page: str) -> None:
    mock_has_internet.return_value = False
    result = can_access_google_page(valid_internet_page)
    assert result == "Not accessible"
    mock_has_internet.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_not_valid_url(mock_valid_google_url: mock.Mock,
                       wrong_internet_page: str) -> None:
    mock_valid_google_url.return_value = False
    result = can_access_google_page(wrong_internet_page)
    assert result == "Not accessible"
    mock_valid_google_url.assert_called_once_with(wrong_internet_page)
