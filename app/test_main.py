import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.fixture()
def mock_has_internet_connection() -> bool:
    with patch("app.main.has_internet_connection") as mocked:
        yield mocked


@pytest.fixture()
def mock_valid_google_url() -> bool:
    with patch("app.main.valid_google_url") as mocked:
        yield mocked


def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
