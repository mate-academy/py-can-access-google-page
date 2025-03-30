import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as mock:
        mock.return_value = True
        yield mock


@pytest.fixture
def mock_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as mock:
        mock.return_value = True
        yield mock


def test_can_access_google_page(
        mock_has_internet_connection: bool, mock_valid_google_url: bool
) -> None:

    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Accessible"

    mock_valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"

    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"
