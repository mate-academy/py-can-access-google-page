import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.fixture()
def mock_function() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        with mock.patch("app.main.has_internet_connection") as mock_internet:
            yield mock_url, mock_internet


def test_can_access_google_page_when_url_valid_and_connection_exists(
        mock_function: tuple
) -> None:
    mock_url, mock_internet = mock_function
    mock_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_no_internet(mock_function: tuple) -> None:
    mock_url, mock_internet = mock_function
    mock_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_invalid_url(mock_function: tuple) -> None:
    mock_url, mock_internet = mock_function
    mock_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://www.invalid-url.com")
    assert result == "Not accessible"


def test_can_access_google_page_when_url_valid_and_connection_not_exist(
        mock_function: tuple
) -> None:
    mock_url, mock_internet = mock_function
    mock_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://www.invalid-url.com")
    assert result == "Not accessible"
