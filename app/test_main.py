import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_functions() -> None:
    with (
        patch("app.main.has_internet_connection")
        as mock_has_internet_connection,
        patch("app.main.valid_google_url")
        as mock_valid_google_url
    ):
        yield {
            "valid_google_url": mock_valid_google_url,
            "has_internet_connection": mock_has_internet_connection
        }


def test_can_access_google_page_accessible(mock_functions: dict) -> None:
    mocks = mock_functions
    mocks["valid_google_url"].return_value = True
    mocks["has_internet_connection"].return_value = True

    assert (
        can_access_google_page("https://www.google.com") == "Accessible"
    )


def test_can_access_google_page_no_internet(mock_functions: dict) -> None:
    mocks = mock_functions
    mocks["valid_google_url"].return_value = True
    mocks["has_internet_connection"].return_value = False

    assert (
        can_access_google_page("https://www.google.com") == "Not accessible"
    )


def test_can_access_google_page_invalid_url(mock_functions: dict) -> None:
    mocks = mock_functions
    mocks["valid_google_url"].return_value = False
    mocks["has_internet_connection"].return_value = True

    assert (
        can_access_google_page(
            "https://www.invalid-url.com"
        ) == "Not accessible"
    )


def test_can_access_google_page_no_internet_and_invalid_url(
        mock_functions: dict
) -> None:
    mocks = mock_functions
    mocks["valid_google_url"].return_value = False
    mocks["has_internet_connection"].return_value = False

    assert (
        can_access_google_page(
            "https://www.invalid-url.com"
        ) == "Not accessible"
    )
