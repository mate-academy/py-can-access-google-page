import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_validations() -> None:
    with (
        patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        with patch("app.main.valid_google_url") as mock_valid_google_url:
            yield mock_valid_google_url, mock_has_internet_connection


def test_can_access_google_page_accessible(mock_validations: str) -> None:
    mock_valid_google_url, mock_has_internet_connection = mock_validations
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_no_internet(mock_validations: str) -> None:
    mock_valid_google_url, mock_has_internet_connection = mock_validations
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_invalid_url(mock_validations: str) -> None:
    mock_valid_google_url, mock_has_internet_connection = mock_validations
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert (
        can_access_google_page("https://www.invalid-url.com")
        == "Not accessible"
    )


def test_can_access_google_page_no_internet_and_invalid_url(
        mock_validations: str
) -> None:
    mock_valid_google_url, mock_has_internet_connection = mock_validations
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert (
        can_access_google_page("https://www.invalid-url.com")
        == "Not accessible"
    )
