import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> "patch":
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def mock_has_internet_connection() -> "patch":
    with patch("app.main.has_internet_connection") as mock:
        yield mock


def test_can_access_google_page_accessible(
        mock_valid_google_url: "patch",
        mock_has_internet_connection: "patch"
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    url = "http://www.google.com"
    result = can_access_google_page(url)

    assert result == "Accessible"


def test_can_access_google_page_not_accessible_invalid_url(
        mock_valid_google_url: "patch",
        mock_has_internet_connection: "patch"
) -> None:

    mock_valid_google_url.return_value = False
    url = "http://invalidurl"
    result = can_access_google_page(url)

    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_no_internet_connection(
        mock_valid_google_url: "patch",
        mock_has_internet_connection: "patch"
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    url = "http://www.google.com"
    result = can_access_google_page(url)

    assert result == "Not accessible"
